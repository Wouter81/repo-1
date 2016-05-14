import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Videos','http://xite.nl/videos/1',221,'','') 
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<img src="(.*?)" />.*?<h3>(.*?)</h3>.*?<a href="(.*?)"><span>Bekijk video</span></a>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for img, name, videopage in match:
        name = utils.cleantext(name)
        videopage = "http://xite.nl" + videopage
        utils.addDownLink(name, videopage, 222, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
#    if len(match) == 15:
#        npage = page + 1        
#        url = url.replace('/'+str(page)+'/','/'+str(npage)+'/')
#        utils.addDir('Volgende Pagina ('+str(npage)+')', url, 221, '', npage)
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile('<source type="video/mp4"  src="(.*?)">', re.DOTALL | re.IGNORECASE).findall(listhtml)
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

