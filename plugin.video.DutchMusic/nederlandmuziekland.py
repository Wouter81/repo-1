import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Seizoen 3','http://www.kijk.nl/ajax/section/series/series-nederlandmuziekland.sbs6-season-3/1/10',270,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/nederland-muziekland.png')
    utils.addDir('Seizoen 2','http://www.kijk.nl/ajax/section/series/series-nederlandmuziekland.sbs6-season-2/1/10',270,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/nederland-muziekland.png')
    utils.addDir('Seizoen 1','http://www.kijk.nl/ajax/section/series/series-nederlandmuziekland.sbs6-season-1/1/10',270,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/nederland-muziekland.png')    
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<noscript><img src="([^"]+)" alt="([^"]+)".*?<a href="([^"]+)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, name, videopage in match:
        name = utils.cleantext(name)
        videopage = "http://www.kijk.nl" + videopage
        utils.addDownLink(name, videopage, 271, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile('<meta property="og:url" content="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")      
    if match:
        videourl = match[0]
        try:     
            import youtubedl
        except Exception:
            xbmc.executebuiltin("XBMC.Notification(DutchMusic,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000,"")")
            return
        xbmc.log(str(videourl))
        videourl=youtubedl.single_YD(videourl)
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

