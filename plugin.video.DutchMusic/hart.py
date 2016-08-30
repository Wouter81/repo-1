import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


#def Main():
#    utils.addDir('Programma Gemist','http://www.omroepbrabant.nl/Uitzendinggemist.aspx?type=tv&id=1276',227,'','')    
#    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2('http://www.omroepbrabant.nl/Uitzendinggemist.aspx?type=tv&id=1276')
    match = re.compile('<span class="date-time">([^<]+)<em>([^<]+)</em></span>([^\t]+).+?<img src=".([^"]+)".*?<a href="(/[^"]+)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for datum, tijd, name, img, videopage in match:
        name = datum + ' ' + tijd + ' - ' + name
        img = "http://www.omroepbrabant.nl" + img
        videopage = "http://www.omroepbrabant.nl" + videopage
        utils.addDownLink(name, videopage, 228, img, '')
    try:
        page = page + 1
        nextp=re.compile('href="([^"]+)">Vol', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://www.omroepbrabant.nl" + nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 227,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png', page, fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml(url,'')
    xmllink = re.compile("clipXmlUrl=([^&]+)&", re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    xmlcontent = utils.getHtml(xmllink,'')
    match = re.compile('MP4_HD".*?src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(xmlcontent)[-1]
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")  
    if match:
        videourl = match
        videourl = videourl.replace("&amp;","&")
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