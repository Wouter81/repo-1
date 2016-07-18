import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Oranje Top 30','http://www.truckerstop12.com/',263,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('href="http://www.truckerstop12.com/video/.*?aflevering.*?vanaf+(.*?)".*?src="http://www.youtube.com/embed/(.*?)?fs=1', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name, videopage in match:
            name = 'Truckers Top 12:' + name.replace('+',' ')
            img = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/truckers-top20.png'
            videopage = "plugin://plugin.video.youtube/play/?video_id=" + videopage.replace('?','')
            utils.addDownLink(name, videopage, 300, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)