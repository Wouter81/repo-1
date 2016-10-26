import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Slam','http://www.slam.nl/slam40/',241,'https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/xite.png','',fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('Spotify app</a>!<br />(.*?)<div class="col-lg-4 col-sm-12">', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for lijst in match:
        match1 = re.compile('<div class="nmbr">(.*?)</div>.*?src="(.*?)".*?title">(.*?)</div>.*?excerpt">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(lijst)
        for nummer, img, titel, artiest in match1:
            name = nummer + '. ' + artiest + ' - ' + titel
            url = artiest + ' ' + titel
            url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
            utils.addDir(name, url, '', img, '', fanart='https://raw.githubusercontent.com/jericho-2016/Jericho/master/plugin.video.jericho/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)