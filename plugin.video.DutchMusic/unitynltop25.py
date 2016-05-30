import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Unity NL Top 25','http://www.unity.nu/Programmas/UnityNL',237,'',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<span class="badge .*?">(.+?)</span>.+?<h4 class="media-heading">(.+?)</h4>.+?<span class="pull-left">(.+?)</span>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for nummer, song, artist in match:
        song = song.replace("&amp;","&")
        artist = artist.replace("&amp;","&")
        name = nummer + '. ' + artist + ' - ' + song
        url = artist + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png', '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    

    