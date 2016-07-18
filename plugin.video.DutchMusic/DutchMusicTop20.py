import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def List(url):
    listhtml = utils.getHtml2('https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/xml/DutchMusicTop20.txt')
    match = re.compile("v=([^\t]+)\t[^\t]+\t\t([^\n]+)", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for utube, name in match:
        url = utube
        url = 'plugin://plugin.video.youtube/play/?video_id=' + urllib.quote_plus(url)
        utils.addDownLink(name, url, 300, 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/logo-video.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)