#-*- coding: utf-8 -*-

'''
    NOS Rio 2016
    Copyright (C) 2016 Patrick Dijkkamp

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


__scriptname__ = "NOS Rio 2016"
__author__ = "Patrick Dijkkamp"
__scriptid__ = "plugin.video.nosrio2016"
__version__ = "1.0.2"

import urllib,urllib2,re, cookielib, urlparse, httplib
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,sys,time, os, gzip, socket

try:
    import json
except:
    import simplejson as json
    

dialog = xbmcgui.Dialog()
addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon(id=__scriptid__)

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)

profileDir = addon.getAddonInfo('profile')
profileDir = xbmc.translatePath(profileDir).decode("utf-8")
cookiePath = os.path.join(profileDir, 'cookies.lwp')

if not os.path.exists(profileDir):
    os.makedirs(profileDir)

urlopen = urllib2.urlopen
cj = cookielib.LWPCookieJar()
Request = urllib2.Request

if cj != None:
    if os.path.isfile(xbmc.translatePath(cookiePath)):
        try:
            cj.load(xbmc.translatePath(cookiePath))
        except:
            try:
                os.remove(xbmc.translatePath(cookiePath))
                pass
            except:
                dialog.ok('Oh oh','The Cookie file is locked, please restart Kodi')
                pass
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
else:
    opener = urllib2.build_opener()

urllib2.install_opener(opener)

API_URL = 'http://ida.omroep.nl/aapi/?stream='
BASE_URL = 'http://livestreams.omroep.nl'
REF_URL = 'http://www.npo.nl'
TOKEN_URL = 'http://ida.omroep.nl/npoplayer/i.js'


def HOOFDMENU():
    headers2 = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive',
           'X-Requested-With': 'XMLHttpRequest',
           'Cookie': 'DNT: 1'}
    livejson = getHtml('http://nos.nl/rio2016/live/','http://nos.nl/rio2016/', headers2)
    try:
        livejson = json.loads(livejson)
        streamlijst = livejson["live"]
        for stream in streamlijst:
            try:
                einde = stream["end_at"]
                einde = re.compile(r"\d{2}:\d{2}", re.DOTALL | re.IGNORECASE).findall(einde)[0]         
                naam = "["+stream["title"].upper() + "] tot "+ kleurtje(einde, "red") + ": " + stream["description"].replace('\n',' ')
                naam = naam.encode('utf-8')
                url = stream["channel"]["stream"]
                img = stream["stream_icon"]["formats"]["url"]["png"]
                addDownLink(naam, url, 2, img)
            except: pass
    except: pass
    try:
        addDownLink('------ Straks --------', '', '', '')
        strakslijst = livejson["upcoming"]
        for straks in strakslijst:
            try:
                start = straks["start_at"]
                start = re.compile(r"\d{2}:\d{2}", re.DOTALL | re.IGNORECASE).findall(start)[0]        
                naam = kleurtje(start, "green") + " ["+straks["title"].upper() + "] " + straks["description"].replace('\n',' ')
                naam = naam.encode('utf-8')
                url = straks["channel"]["stream"]
                img = straks["stream_icon"]["formats"]["url"]["png"]
                addDownLink(naam, url, 2, img)
            except: pass
    except:
        addDownLink('Geen streams of aankomende streams', '', '', '')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def kleurtje(tekst, kleur):
    tekst = "[COLOR " + kleur + "]" + tekst + "[/COLOR]"
    return tekst

def VIDEOLINKS(url,name):
    videourl = streamNpo(url)
    xbmc.log(videourl)
    iconimage = xbmc.getInfoImage("ListItem.Thumb")
    listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    listitem.setInfo('video', {'Title': name})
    xbmc.Player().play(videourl, listitem)

def collect_token():
    req = urllib2.Request(TOKEN_URL)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    token = re.search(r'npoplayer.token = "(.*?)"',page).group(1)
    first = -1
    last = -1
    for i in range(5, len(token) - 5, 1):
        if token[i].isdigit():
            if first < 0:
                first = i
            elif last < 0:
                last = i
                break
    newtoken = list(token)
    if first < 0 or last < 0:
        first = 12
        last = 13
    newtoken[first] = token[last]
    newtoken[last] = token[first]
    newtoken = ''.join(newtoken)
    return newtoken
    
def resolve_http_redirect(url, depth=0):
    if depth > 10:
        raise Exception("Redirected "+depth+" times, giving up.")
    o = urlparse.urlparse(url,allow_fragments=True)
    conn = httplib.HTTPConnection(o.netloc)
    path = o.path
    if o.query:
        path +='?'+o.query
    conn.request("HEAD", path)
    res = conn.getresponse()
    headers = dict(res.getheaders())
    if headers.has_key('location') and headers['location'] != url:
        return resolve_http_redirect(headers['location'], depth+1)
    else:
        return url
    
def streamNpo(source):
    URL=API_URL+BASE_URL+source+"&token=%s" % collect_token()
    req = urllib2.Request(URL)
    req.add_header('User-Agent', USER_AGENT)
    req.add_header('Referer', REF_URL)
    response = urllib2.urlopen(req)
    page = response.read()
    response.close()
    videopre=re.search(r'http:(.*?)url',page).group()
    prostream= (videopre.replace('\/', '/'))
    xbmc.log(prostream)
    finalUrl = resolve_http_redirect(prostream)
    return finalUrl


def getHtml(url, referer='', hdr=None, NoCookie=None, data=None):
    if not hdr:
        req = Request(url, data, headers)
    else:
        req = Request(url, data, hdr)
    if len(referer) > 1:
        req.add_header('Referer', referer)
    if data:
        req.add_header('Content-Length', len(data))
    response = urlopen(req, timeout=60)
    if response.info().get('Content-Encoding') == 'gzip':
        buf = StringIO( response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = f.read()
        f.close()
    else:
        data = response.read()    
    if not NoCookie:
        # Cope with problematic timestamp values on RPi on OpenElec 4.2.1
        try:
            cj.save(cookiePath)
        except: pass
    response.close()
    return data

    
def postHtml(url, form_data={}, headers={}, compression=True):
    _user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 ' + \
                  '(KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'
    req = urllib2.Request(url)
    if form_data:
        form_data = urllib.urlencode(form_data)
        req = urllib2.Request(url, form_data)
    req.add_header('User-Agent', _user_agent)
    for k, v in headers.items():
        req.add_header(k, v)
    if compression:
        req.add_header('Accept-Encoding', 'gzip')
    response = urllib2.urlopen(req)
    data = response.read()
    cj.save(cookiePath)
    response.close()
    return data


def getParams():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if params[len(params) - 1] == '/':
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


def addDownLink(name,url,mode,iconimage):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name })
    video_streaminfo = {'codec': 'h264'}
    liz.addStreamInfo('video', video_streaminfo)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok


def addDir(name,url,mode,iconimage):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name })
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok




params = getParams()
url = None
name = None
mode = None
download = None

try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass



if mode == None: HOOFDMENU()
elif mode == 1: INDEX(url,1)
elif mode == 2: VIDEOLINKS(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
