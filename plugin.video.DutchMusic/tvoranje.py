import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Programma Gemist','http://www.tvoranje.nl/?p=84&p2=1',221,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/tvoranje.png')
    utils.addDir('Showflitsen','http://www.tvoranje.nl/?p=9&p2=1',221,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/tvoranje.png')    
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<div class="news_title">(.+?)</div>.+?<div class="news_summary_thumb_container"><img src="(.+?)" alt="" class="news_summary_image" /></div>.+?<div class="news_readmore"><a href="(.+?)">Lees verder &raquo;</a></div>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for name, img, videopage in match:
        name = utils.cleantext(name)
        img = "http://www.tvoranje.nl" + img
        videopage = "http://www.tvoranje.nl" + videopage
        utils.addDownLink(name, videopage, 222, img, '')
    try:
        page = page + 1
        nextp=re.compile('href="([^"]+)"> Vol', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://www.tvoranje.nl" + nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 221,'', page)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile('<video src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")  
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

