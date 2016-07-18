import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Oranje Top 30','http://oranjetop30.nl/',255,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('a href="(.*?)"><img border="0" src="bekijk1.png" style="margin-bottom:2px;" /></a><br/>.*?value="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    if match:
        for videopage, name in match:
            if 'Week' in name:
                name = 'Uitzending: ' + utils.cleantext(name)
                videopage = "http://www.oranjetop30.nl/" + videopage.replace(' ','%20')
                return name, videopage
    else:
        name = 'De uitzending van deze week is nog niet beschikbaar, probeer het later nog eens.'
        return name, 'http://oranjetop30.nl/'


def Playvid(url, name):
    listhtml = utils.getHtml(url, url)
    match = re.compile('src: "(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")  
    if match:
        videourl = 'http://www.oranjetop30.nl/' + match[0]
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
        utils.notify('De uitzending van deze week is nog niet beschikbaar!','Probeer het later nog eens.')

