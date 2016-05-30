import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('XML','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/xml/karaoke.xml',239,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(zoekwoord):
    listhtml = utils.getHtml2('https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/xml/karaoke.xml')
    match = re.compile('<item>(.*?)</item>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for lijst in match:
        if re.search(zoekwoord, lijst, re.DOTALL | re.IGNORECASE):
            match1 = re.compile('<title>(.*?)</title>.*?<utube>(.*?)</utube>.*?<thumbnail>(.*?)</thumbnail>', re.DOTALL | re.IGNORECASE).findall(lijst)
            for name, utube, img in match1:
                url = utube
                url = 'plugin://plugin.video.youtube/play/?video_id=' + urllib.quote_plus(url)
                utils.addDownLink(name, url, 300, img, '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
 
def Search():
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    List(vq)