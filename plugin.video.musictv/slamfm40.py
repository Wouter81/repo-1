import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3

addon = xbmcaddon.Addon('plugin.video.musictv')
addonname = addon.getAddonInfo('name')
addon_id = 'plugin.video.musictv'
selfAddon = xbmcaddon.Addon(id=addon_id)
profile_path =  xbmc.translatePath(selfAddon.getAddonInfo('profile'))
home = xbmc.translatePath(addon.getAddonInfo('path').decode('utf-8')) 
icon = os.path.join(home, 'icon.png')
fanart = os.path.join(home, 'fanart.png')


def Main():
    utils.addDir('Slam','http://www.slam.nl/slam40/',241,'','',fanart=fanart)
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
            utils.addDir(name, url, '', img, '', fanart=fanart)
    xbmcplugin.endOfDirectory(utils.addon_handle)