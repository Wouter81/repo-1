#-*- coding: utf-8 -*-

import urllib,urllib2,re, cookielib, urlparse, httplib
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,sys,time, os, gzip, socket
import time, datetime
from datetime import date, datetime, timedelta

try:
    import json
except:
    import simplejson as json
    


addon = xbmcaddon.Addon('plugin.video.luckytv')
addonname = addon.getAddonInfo('name')
addon_id = 'plugin.video.luckytv'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8')) 
icon = os.path.join(home, 'icon.png')
fanart = os.path.join(home, 'fanart.jpg')


addon_handle = int(sys.argv[1])
pluginhandle = int(sys.argv[1])


luckyzoeken = 'http://www.luckytv.nl/afleveringen/page/1/?q='
afleveringen ='http://www.luckytv.nl/afleveringen/page/1/'
hetbeste ='http://www.luckytv.nl/het-beste/page/1/'
willy ='http://www.luckytv.nl/willy-en-max/page/1/'

def getHtml(url, referer=None, hdr=None, data=None):
    USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
    headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
    if not hdr:
        req = urllib2.Request(url, data, headers)
    else:
        req = urllib2.Request(url, data, hdr)
    if referer:
        req.add_header('Referer', referer)
    response = urllib2.urlopen(req, timeout=60)
    data = response.read()    
    response.close()
    return data


def MainDir():
    addDir('Afleveringen' ,afleveringen,1,icon)
    addDir('Het Beste' ,hetbeste,1,icon)
    addDir('Willy' ,willy,1,icon)
    addDir('Zoeken' ,luckyzoeken,2,icon)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def luckyread(url, page=None):
    listhtml = getHtml(url,url)
    match = re.compile('<img class="video__thumb".*?src="(.*?)".*?<a class="video__title" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, videopage, name in match:
        name = cleantext(name)
        name = striphtml(name)
        addLink(name,videopage,20,img,fanart)
    try:
        if len(match) == 24:
            npage = page + 1        
            url = url.replace('page/'+str(page)+'/','page/'+str(npage)+'/')
            addDir('Volgende Pagina ('+str(npage)+')', url, 1, icon, npage)
    except:
        pass
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
    

def luckysearch(url, page=1):
    listhtml = getHtml(url,url)
    match = re.compile('<img class="video__thumb".*?src="(.*?)".*?<a class="video__title" href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    if match:
        for img, videopage, name in match:
            name = cleantext(name)
            name = striphtml(name)
            addLink(name,videopage,20,img,fanart)

        if len(match) == 24:
            npage = page + 1        
            url = url.replace('page/'+str(page)+'/?q=','page/'+str(npage)+'/?q=')
            addDir('Volgende Pagina ('+str(npage)+')', url, 3, icon, npage)

    else:
        notify('LuckyTV', 'Er zijn geen resultaten gevonden.')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        
def notify(header=None, msg='', duration=5000):
    if header is None: header = 'DutchMusic'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, icon)
    xbmc.executebuiltin(builtin)
        
def Play(url,name):
    listhtml = getHtml(url,url)
    match = re.compile('"contentUrl": "(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    dp.create("LuckyTV","Een ogenblik geduld.")  
    if match:
        videourl = match[0]
        videourl = videourl.replace(" ","%20")
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Music'})
        listitem.setProperty("IsPlayable","true")
        if int(sys.argv[1]) == -1:
            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            pl.clear()
            pl.add(videourl, listitem)
            xbmc.Player().play(pl)
        else:
            listitem.setPath(str(videourl))
            xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)
    else:
        utils.notify('Oh oh','Couldn\'t find a playable video link')

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


def addLink(name,url,mode,iconimage,fanartimage):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name })
    video_streaminfo = {'codec': 'h264'}
    liz.addStreamInfo('video', video_streaminfo)
    liz.setProperty("Fanart_Image", fanartimage)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok

def addDir(name,url,mode,iconimage,page=None):
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&page=" + str(page) +
         "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={ "Title": name })
    liz.setProperty("Fanart_Image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def cleantext(text):
    text = text.replace('&#8211;','-')
    text = text.replace('&#038;','&')
    text = text.replace('&#8217;','\'')
    text = text.replace('&#8216;','\'')
    text = text.replace('&#8230;','...')
    text = text.replace('&quot;','"')
    text = text.replace('&#039;','`')
    text = text.replace('&amp;','&')
    text = text.replace('&ntilde;','ñ')
    return text

def _get_keyboard(default="", heading="", hidden=False):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return unicode(keyboard.getText(), "utf-8")
    return default

def search(url):
    searchUrl = url
    vq = _get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','+')
    searchUrl = searchUrl + title
    #page = page=None
    print "Searching URL: " + searchUrl
    xbmc.log(searchUrl)
    luckysearch(searchUrl) 
    
def striphtml(data):
    p = re.compile(r'<.*?>', 
    re.DOTALL | re.IGNORECASE)
    return p.sub('', data)

params = getParams()
url = None
name = None
mode = None
page = 1
download = None

try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass
try: page = int(params["page"])
except: pass



if mode == None: MainDir()
elif mode == 1: luckyread(url, page)
elif mode == 2: search(url)
elif mode == 3: luckysearch(url, page)

elif mode == 20: Play(url,name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))