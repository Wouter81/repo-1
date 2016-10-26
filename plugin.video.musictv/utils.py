#-*- coding: utf-8 -*-

import urllib, urllib2, re, cookielib, os.path, sys, socket, time, tempfile, string
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, sqlite3

from StringIO import StringIO
import gzip

__scriptname__ = "DOKITV"
__author__ = "DOKITV"
__scriptid__ = "plugin.video.musictv"
__credits__ = "DOKITV"
__version__ = "1.0.0"

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
           

addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon(id=__scriptid__)

progress = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()

rootDir = addon.getAddonInfo('path')
if rootDir[-1] == ';':
    rootDir = rootDir[0:-1]
rootDir = xbmc.translatePath(rootDir)
resDir = os.path.join(rootDir, 'resources')
imgDir = os.path.join(resDir, 'images')
nlvicon = xbmc.translatePath(os.path.join(rootDir, 'icon.png'))

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

favoritesdb = os.path.join(profileDir, 'favorites.db')


            
def notify(header=None, msg='', duration=5000):
    if header is None: header = 'DutchMusic'
    builtin = "XBMC.Notification(%s,%s, %s, %s)" % (header, msg, duration, dmicon)
    xbmc.executebuiltin(builtin)


def getHtml(url, referer, hdr=None, NoCookie=None, data=None):
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

   
def getHtml2(url):
    req = Request(url)
    response = urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data 

    
def getVideoLink(url, referer):
    req2 = Request(url, '', headers)
    req2.add_header('Referer', referer)
    url2 = urlopen(req2).geturl()
    return url2


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
    text = text.replace("&#39;","'")
    text = text.replace('&#233;','é')
    text = text.replace('&#252;','ü')
    text = text.replace('&nbsp;',' ')
    text = text.replace('&iacute;','í')
    text = text.replace('&acute;','´')
    text = text.replace('&bull;','-')
    text = text.replace('&ndash;','-')
    return text


def addDownLink(name, url, mode, iconimage, desc, stream=None, fav='add', fanart=None):
    if fav == 'add': favtext = "Add to"
    elif fav == 'del': favtext = "Remove from"
    u = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&name=" + urllib.quote_plus(name))
    dwnld = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&mode=" + str(mode) +
         "&download=" + str(1) +
         "&name=" + urllib.quote_plus(name))
    favorite = (sys.argv[0] +
         "?url=" + urllib.quote_plus(url) +
         "&fav=" + fav +
         "&favmode=" + str(mode) +
         "&mode=" + str('900') +
         "&img=" + urllib.quote_plus(iconimage) +
         "&name=" + urllib.quote_plus(name))         
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    if stream:
        liz.setProperty('IsPlayable', 'true')
    if len(desc) < 1:
        liz.setInfo(type="Video", infoLabels={"Title": name})
    else:
        liz.setInfo(type="Video", infoLabels={"Title": name, "plot": desc, "plotoutline": desc})
    if fanart:
        liz.setArt({'fanart': fanart})
    liz.addContextMenuItems([('[COLOR lime]Download Video[/COLOR]', 'xbmc.RunPlugin('+dwnld+')'),
    ('[COLOR lime]' + favtext + ' favorites[/COLOR]', 'xbmc.RunPlugin('+favorite+')')])
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=False)
    return ok
    
def playyt(url, name):
    iconimage = xbmc.getInfoImage("ListItem.Thumb")
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    dp = xbmcgui.DialogProgress()
    dp.create("Jericho","Please wait")  
    xbmc.Player().play(url, liz, False)

def addDir(name, url, mode, iconimage, page=None, channel=None, section=None, keyword='', Folder=True, fanart=None):
    if url.startswith("plugin://"):
        u = url
    else:
        u = (sys.argv[0] +
             "?url=" + urllib.quote_plus(url) +
             "&mode=" + str(mode) +
             "&page=" + str(page) +
             "&channel=" + str(channel) +
             "&section=" + str(section) +
             "&keyword=" + urllib.quote_plus(keyword) +
             "&name=" + urllib.quote_plus(name))
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setArt({'thumb': iconimage, 'icon': iconimage})
    if fanart:
        liz.setArt({'fanart': fanart})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    ok = xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=liz, isFolder=Folder)
    return ok
    
def _get_keyboard(default="", heading="", hidden=False):
    """ shows a keyboard and returns a value """
    keyboard = xbmc.Keyboard(default, heading, hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        return unicode(keyboard.getText(), "utf-8")
    return default
 