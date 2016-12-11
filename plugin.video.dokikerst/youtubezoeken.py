import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('TXT','http://addon.dokitv.nl/kerst/DOKITV%20Kerst%20Playlist.txt',239,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(zoekwoord):
    listhtml = utils.getHtml2('http://addon.dokitv.nl/kerst/DOKITV%20Kerst%20Playlist.txt')
    match = re.compile("v=([^\t]+)\t[^\t]+\t\t([^\n]+)", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for utube, name in match:
        if re.search(zoekwoord, name, re.DOTALL | re.IGNORECASE):
            url = utube
            url = 'plugin://plugin.video.youtube/play/?video_id=' + urllib.quote_plus(url)
            utils.addDownLink(name, url, 300, 'http://addon.dokitv.nl/kerst/icon.jpg', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
 
def Search():
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    List(vq)