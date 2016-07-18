import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Artiesten Zoeken','http://www.radionl.fm/wp-content/themes/radionl2/archive-cpt_artiesten-search.php?term=',253,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png')
    utils.addDir('Populaire Artiesten','http://www.radionl.fm/artiesten/',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png')
    utils.addDir('0-9','http://www.radionl.fm/artiesten/?sort=0-9',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png')
    for i in map(chr, range(97, 123)):
        utils.addDir(i.upper(),'http://www.radionl.fm/artiesten/?sort='+i,250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListArtist(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<div class="artistBox.*?">.*?<img src="(.*?)".*?<div class="name"><a href="(.*?)" title="">(.*?)</a>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for img, url, artist in match:
        img = 'http://radionl.fm' + img
        url = 'http://www.radionl.fm' + url
        utils.addDir(artist, url, 251, img)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListSong(name, url, iconimage):
    listhtml = utils.getHtml2(url)
    match = re.compile('<div class="titel"><div class="titel_naam">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for song in match:
        url = name + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(song, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListSearch(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('value":"(.*?)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for artist in match:
        url = 'http://www.radionl.fm/artiesten/' + artist.replace(' ','-').replace('\/','/')
        name = artist.replace('\/','/')
        utils.addDir(name, url, 251, 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','%20')
    searchUrl = searchUrl + title
    print "Searching URL: " + searchUrl
    ListSearch(searchUrl)