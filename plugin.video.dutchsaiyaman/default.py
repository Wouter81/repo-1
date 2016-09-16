'''
    Dutch Saiyaman
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


__scriptname__ = "Dutch Saiyaman"
__author__ = "Patrick Dijkkamp"
__scriptid__ = "plugin.video.dutchsaiyaman"
__version__ = "1.0.3"

import urllib,urllib2,re, gzip, socket, cookielib
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,sys,time, os

from jsunpack import unpack

dialog = xbmcgui.Dialog()
progress = xbmcgui.DialogProgress()
addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon(id=__scriptid__)
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
socket.setdefaulttimeout(60)

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)
dsicon = xbmc.translatePath(os.path.join(rootDir, 'icon.png'))
bokuicon = xbmc.translatePath(os.path.join(rootDir, 'BokuNoHeroAcademia.png'))
dbsicon = xbmc.translatePath(os.path.join(rootDir, 'DragonBallSuper.png'))
pmicon = xbmc.translatePath(os.path.join(rootDir, 'PocketMonstersTheOrigin.png'))
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

def notify(header=None, msg='', duration=5000):
    if header is None: header = 'Dutch Saiyaman'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, dsicon)
    xbmc.executebuiltin(builtin)
    

def PLAYVIDEO(url, name, download=None):
    progress.create('Play video', 'Searching videofile.')
    progress.update( 10, "", "Loading video page", "" )
    videosource = getHtml(url, url)
    playvideo(videosource, name, download, url)


def playvideo(videosource, name, download=None, url=None):
    hosts = []
    if re.search('videomega\.tv/', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('VideoMega')
    if re.search('<source', videosource, re.DOTALL | re.IGNORECASE):
        hosts.append('DS')        
    
    if len(hosts) == 0:
        progress.close()
        notify('Oh oh','Couldn\'t find any video')
        return
    elif len(hosts) > 1:
        if addon.getSetting("dontask") == "true":
            vidhost = hosts[0]            
        else:
            vh = dialog.select('Videohost:', hosts)
            vidhost = hosts[vh]
    else:
        vidhost = hosts[0]
    
    if vidhost == 'VideoMega':
        progress.update( 40, "", "Loading videomegatv", "" )
        if re.search("videomega.tv/iframe.js", videosource, re.DOTALL | re.IGNORECASE):
            hashref = re.compile("""javascript["']>ref=['"]([^'"]+)""", re.DOTALL | re.IGNORECASE).findall(videosource)
        elif re.search("videomega.tv/iframe.php", videosource, re.DOTALL | re.IGNORECASE):
            hashref = re.compile(r"iframe\.php\?ref=([^&]+)&", re.DOTALL | re.IGNORECASE).findall(videosource)
        elif re.search("videomega.tv/view.php", videosource, re.DOTALL | re.IGNORECASE):
            hashref = re.compile(r'view\.php\?ref=([^"]+)', re.DOTALL | re.IGNORECASE).findall(videosource)
        elif re.search("videomega.tv/cdn.php", videosource, re.DOTALL | re.IGNORECASE):
            hashref = re.compile(r'cdn\.php\?ref=([^"]+)', re.DOTALL | re.IGNORECASE).findall(videosource)
        elif re.search("videomega.tv/\?ref=", videosource, re.DOTALL | re.IGNORECASE):
            hashref = re.compile(r'videomega.tv/\?ref=([^"]+)', re.DOTALL | re.IGNORECASE).findall(videosource)
        else:
            hashkey = re.compile("""hashkey=([^"']+)""", re.DOTALL | re.IGNORECASE).findall(videosource)
            if not hashkey:
                notify('Oh oh','Couldn\'t find playable videomega link')
                return
            hashkey = chkmultivids(hashkey)
            hashpage = getHtml('http://videomega.tv/validatehash.php?hashkey='+hashkey, url)
            hashref = re.compile('ref="([^"]+)', re.DOTALL | re.IGNORECASE).findall(hashpage)
        progress.update( 80, "", "Getting video file from Videomega", "" )
        vmhost = 'http://videomega.tv/view.php?ref=' + hashref[0]
        videopage = getHtml(vmhost, url)
        vmpacked = re.compile(r"(eval\(.*\))\s+</", re.DOTALL | re.IGNORECASE).findall(videopage)
        vmunpacked = unpack(vmpacked[0])
        videourl = re.compile('src",\s?"([^"]+)', re.DOTALL | re.IGNORECASE).findall(vmunpacked)
        videourl = videourl[0]
        videourl = videourl + '|Referer=' + vmhost + '&User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
    if vidhost == 'DS':
        progress.update( 80, "", "Getting video file from DutchSaiyaman", "" )
        videourl = re.compile('<source.*?src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(videosource)[0]
    progress.close()
    playvid(videourl, name, download)


def playvid(videourl, name, download=None):
    if download == 1:
        downloadVideo(videourl, name)
    else:
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name})
        xbmc.Player().play(videourl, listitem)


def chkmultivids(videomatch):
    videolist = list(set(videomatch))
    if len(videolist) > 1:
        i = 1
        hashlist = []
        for x in videolist:
            hashlist.append('Video ' + str(i))
            i += 1
        mvideo = dialog.select('Multiple videos found', hashlist)
        return videolist[mvideo]
    else:
        return videomatch[0]

def getHtml(url, referer=None, hdr=None, NoCookie=None, data=None):
    if not hdr:
        req = Request(url, data, headers)
    else:
        req = Request(url, data, hdr)
    if referer:
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
    
def addDownLink(name, url, mode, iconimage):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    fanart = os.path.join(rootDir, 'fanart.jpg')
    liz.setArt({'fanart': fanart})
    video_streaminfo = {'codec': 'h264'}
    liz.addStreamInfo('video', video_streaminfo)    
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=False)
    return ok
    

def addDir(name, url, mode, iconimage, Folder=True):
    if url.startswith('plugin'):
        u = url
    else:
        u = (sys.argv[0] +
             "?url=" + urllib.quote_plus(url) +
             "&mode=" + str(mode) +
             "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    fanart = os.path.join(rootDir, 'fanart.jpg')
    liz.setArt({'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok


def INDEX():
    addDir('Dragon Ball Super', 'http://dutchsaiyaman.nl/dragon-ball-super/', 2, dbsicon)
    addDir('Boku no Hero Academia', 'http://dutchsaiyaman.nl/boku-no-hero-academia/', 3, bokuicon)
    addDir('Pocket Monsters: The Origin', 'http://dutchsaiyaman.nl/pocket-monsters-the-origin/', 5, pmicon)
    addDir('Youtube kanaal', 'plugin://plugin.video.youtube/channel/UCXi-QfJ6ul2Ml2LQQCA1J_w/', '', dsicon)
    addDownLink('','','',dsicon)
    addDownLink('Recent uitgebracht:','','',dsicon)
    Laatste()    
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def Laatste():
    laatstepage = getHtml('http://dutchsaiyaman.nl/media/')
    laatste = re.compile("<strong>Recent uitgebracht:<br />(.*)Series", re.DOTALL | re.IGNORECASE).findall(laatstepage)[0]
    laatste1 = re.compile('href="([^"]+)">([^<]+)<', re.DOTALL | re.IGNORECASE).findall(laatste)
    for videopage, naam in laatste1:
        if 'Super' in naam:
            laatsteicon = dbsicon
        elif 'Boku' in naam:
            laatsteicon = bokuicon
        elif 'Pocket' in naam:
            laatsteicon = pmicon
        else:
            laatsteicon = dsicon
        addDownLink(naam, videopage, 4, laatsteicon)


def DBS(url):
    dbspage = getHtml(url)
    dbspart = re.compile('"title">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(dbspage)[0]
    dbslinks = re.compile('href="([^"]+)">([^<]+)<', re.DOTALL | re.IGNORECASE).findall(dbspart)
    for videopage, naam in dbslinks:
        addDownLink(naam, videopage, 4, dbsicon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def MHA(url):
    mhapage = getHtml(url)
    mhapart = re.compile('"title">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(mhapage)[0]
    mhalinks = re.compile('href="([^"]+)">([^<]+)<', re.DOTALL | re.IGNORECASE).findall(mhapart)    
    for videopage, naam in mhalinks:
        addDownLink(naam, videopage, 4, bokuicon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


def PM(url):
    pmpage = getHtml(url)
    pmpart = re.compile('"title">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(pmpage)[0]
    pmlinks = re.compile('href="([^"]+)">([^<]+)<', re.DOTALL | re.IGNORECASE).findall(pmpart)
    for videopage, naam in pmlinks:
        addDownLink(naam, videopage, 4, pmicon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))


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


params = getParams()
url = None
name = None
mode = None
img = None


try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: img = urllib.unquote_plus(params["img"])
except: pass

if mode is None: INDEX()
elif mode == 2: DBS(url)
elif mode == 3: MHA(url)
elif mode == 4: PLAYVIDEO(url, name)
elif mode == 5: PM(url)
elif mode == 6: playvid(url, name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
