import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def List(url):
    url = 'http://sterren-app.npo.nl/top-20/'
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<a class="teaser-link" href="(.*?)">.*?<div class="position-new">\s+(\d+).*?<span class="teaser-subtitle">(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, nummer, muziek in match:
        name = nummer + '. ' + utils.cleantext(muziek)
        img = ''
        videopage = "http://sterren-app.npo.nl" + videopage
        utils.addDownLink(name, videopage, 265, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile('embed/([^\?]+)', re.IGNORECASE | re.DOTALL).findall(listhtml)
    if match:
        videourl = match[0]
        videourl = 'plugin://plugin.video.youtube/play/?video_id=' + urllib.quote_plus(videourl)
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