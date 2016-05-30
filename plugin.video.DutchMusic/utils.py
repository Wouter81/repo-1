#-*- coding: utf-8 -*-

import urllib, urllib2, re, cookielib, os.path, sys, socket, time, tempfile, string
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, sqlite3

from StringIO import StringIO
import gzip

__scriptname__ = "DutchMusic"
__author__ = "DutchMusic"
__scriptid__ = "plugin.video.DutchMusic"
__credits__ = "DutchMusic"
__version__ = "1.0.2"

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
           
openloadhdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
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
dmicon = xbmc.translatePath(os.path.join(rootDir, 'icon.png'))

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
 
 
# function decodeOpenload(html) provide html from embedded openload page, gives back the video url
# if you want to use this, ask me nice :)
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NDIgNTAoMjMpOgoKCSMgNTAgMzggNDYgMjYsIDJjIDM3IDM5IDNkIDJmIDJlIDI5IDopCgkxNSA9IDQ3LmIoMjUiPDEyKD86LnxcMzIpKj88MTZcMzJbXj5dKj8+KCg/Oi58XDMyKSo/KTwvMTYiLCAyMywgNDcuNTEgfCA0Ny4zMCkuNTIoMSkKCgkxNSA9IDE1LjM2KCIxZCIsIiIpCgkxNSA9IDE1LjM2KCIoNDAgKyA0MCArIDRlKSIsICI5IikKCTE1ID0gMTUuMzYoIig0MCArIDQwKSIsIjgiKQoJMTUgPSAxNS4zNigiKDQwICsgKDFhXjMzXjFhKSkiLCI3IikKCTE1ID0gMTUuMzYoIigoMWFeMzNeMWEpICsoMWFeMzNeMWEpKSIsIjYiKQoJMTUgPSAxNS4zNigiKDQwICsgNGUpIiwiNSIpCgkxNSA9IDE1LjM2KCI0MCIsIjQiKQoJMTUgPSAxNS4zNigiKCgxYV4zM14xYSkgLSA0ZSkiLCIyIikKCTE1ID0gMTUuMzYoIigxYV4zM14xYSkiLCIzIikKCTE1ID0gMTUuMzYoIjRlIiwiMSIpCgkxNSA9IDE1LjM2KCIoKyErW10pIiwiMSIpCgkxNSA9IDE1LjM2KCIoY14zM14xYSkiLCIwIikKCTE1ID0gMTUuMzYoIigwKzApIiwiMCIpCgkxNSA9IDE1LjM2KCIxNCIsIlxcIikgIAoJMTUgPSAxNS4zNigiKDMgKzMgKzApIiwiNiIpCgkxNSA9IDE1LjM2KCIoMyAtIDEgKzApIiwiMiIpCgkxNSA9IDE1LjM2KCIoIStbXSshK1tdKSIsIjIiKQoJMTUgPSAxNS4zNigiKC1+LX4yKSIsIjQiKQoJMTUgPSAxNS4zNigiKC1+LX4xKSIsIjMiKQoJMTUgPSAxNS4zNigiKC1+MCkiLCIxIikKCTE1ID0gMTUuMzYoIigtfjEpIiwiMiIpCgkxNSA9IDE1LjM2KCIoLX4zKSIsIjQiKQoJMTUgPSAxNS4zNigiKDAtMCkiLCIwIikKCQoJMTggPSA0Ny5iKDI1IlxcXCsoW14oXSspIiwgMTUsIDQ3LjUxIHwgNDcuMzApLjUyKDEpCgkxOCA9ICJcXCsiKyAxOAoJMTggPSAxOC4zNigiKyIsIiIpCgkxOCA9IDE4LjM2KCIgIiwiIikKCQoJMTggPSAzMSgxOCkKCTE4ID0gMTguMzYoIlxcLyIsIi8iKQoJCgkzYSAnMTEnIDJhIDE4OgoJCTEwID0gNDcuNDgoMjUiMTFcKGFcKyhcZCspIiwgNDcuNTEgfCA0Ny4zMCkuM2UoMTgpWzBdCgkJMTAgPSAyMigxMCkKCQkyMCA9IDQ3LjQ4KDI1IihcKFxkW14pXStcKSkiLCA0Ny41MSB8IDQ3LjMwKS4zZSgxOCkKCQkyZiAxYyAyYSAyMDoKCQkJZiA9IDQ3LjQ4KDI1IihcZCspLChcZCspIiwgNDcuNTEgfCA0Ny4zMCkuM2UoMWMpCgkJCTFmID0gMTAgKyAyMihmWzBdWzBdKQoJCQkxZSA9IDIxKDIyKGZbMF1bMV0pLDFmKQoJCQkxOCA9IDE4LjM2KDFjLDFlKQoJCTE4ID0gMTguMzYoIisiLCIiKQoJCTE4ID0gMTguMzYoIlwiIiwiIikKCQk0OSA9IDQ3LmIoMjUiKDNiW15cfV0rKSIsIDE4LCA0Ny41MSB8IDQ3LjMwKS41MigxKQoJMjQ6CgkJNDkgPSA0Ny5iKDI1IjQ0XDMyPz1cMzI/XCJ8JyhbXlwiJ10rKSIsIDE4LCA0Ny41MSB8IDQ3LjMwKS41MigxKQoJCgkxOSA9ICIxNy4xMi4iICsgIjRiIiArICI0ZiIgKyAiYyIKCTJkID0gIjE3LjEyLiIgKyAiNGMiICsgIjFhIiArICIyNSIgKyAiNTMiICsgImEiICsgImUiICsgIjRhIgoJCgkzYSAxOSAyYSAzNS4xYignM2MnKToKCQk0ZCA9IDQ5CgkyNDoKCQk0ZCA9ICIzNDovLzQzLjI3LjNmLzMyLzEzLzJiLjQxPzQ1PTEiCgkyOCA0ZA==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|6|7|8|9|a|search|c|d|e|match1|base|toString|video|2ds5o61a22srpob|(ﾟДﾟ)[ﾟεﾟ]|aastring|script|plugin|decodestring|check1|o|getAddonInfo|repl|(ﾟДﾟ)[ﾟεﾟ]+(oﾟｰﾟo)+ ((c^_^o)-(c^_^o))+ (-~0)+ (ﾟДﾟ) ['c']+ (-~-~1)+|repl2|base2|match|base10toN|int|html|else|r|mortael|dropbox|return|credit|in|ahahah|please|check2|proper|for|IGNORECASE|decode|s|_|https|addon|replace|leave|made|this|if|http|path|line|findall|com|(ﾟｰﾟ)|mp4|def|www|vr|dl|by|re|compile|videourl|l|u|m|videourl2|(ﾟΘﾟ)|w|decodeOpenLoad|DOTALL|group|t".split("|")))





def decode(encoded):
    for octc in (c for c in re.findall(r'\\(\d{2,3})', encoded)):
        encoded = encoded.replace(r'\%s' % octc, chr(int(octc, 8)))
    return encoded.decode('utf8')


def base10toN(num,n):
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current/n
    return new_num_string