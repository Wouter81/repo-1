import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Oranje Top 30','http://oranjetop30.nl/',235,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile("<img src='dw/([^<]+)gif'/></div><div class='vw'><img src='.+?'/></div>.+?<div class='ti'>([^<]+)<br/><span class='tiNote'>([^<]+)<span class='tiComp'>", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for nummer, song, artist in match:
        artist = artist.decode('latin1').encode('utf8')
        song = song.decode('latin1').encode('utf8')
        name = nummer + ' ' + artist + song
        url = artist + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/oranje-top30.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    

    