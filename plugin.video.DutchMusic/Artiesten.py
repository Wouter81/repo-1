import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Artiesten Zoeken','http://www.radionl.fm/wp-content/themes/radionl2/archive-cpt_artiesten-search.php?term=',253,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Populaire Artiesten','http://www.radionl.fm/artiesten/',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('0-9','http://www.radionl.fm/artiesten/?sort=0-9',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('A','http://www.radionl.fm/artiesten/?sort=a',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('B','http://www.radionl.fm/artiesten/?sort=b',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('C','http://www.radionl.fm/artiesten/?sort=c',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('D','http://www.radionl.fm/artiesten/?sort=d',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('E','http://www.radionl.fm/artiesten/?sort=e',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('F','http://www.radionl.fm/artiesten/?sort=f',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('G','http://www.radionl.fm/artiesten/?sort=g',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('H','http://www.radionl.fm/artiesten/?sort=h',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('I','http://www.radionl.fm/artiesten/?sort=i',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('J','http://www.radionl.fm/artiesten/?sort=j',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('K','http://www.radionl.fm/artiesten/?sort=k',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('L','http://www.radionl.fm/artiesten/?sort=l',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('M','http://www.radionl.fm/artiesten/?sort=m',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('N','http://www.radionl.fm/artiesten/?sort=n',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('O','http://www.radionl.fm/artiesten/?sort=o',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('P','http://www.radionl.fm/artiesten/?sort=p',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Q','http://www.radionl.fm/artiesten/?sort=q',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('R','http://www.radionl.fm/artiesten/?sort=r',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('S','http://www.radionl.fm/artiesten/?sort=s',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('T','http://www.radionl.fm/artiesten/?sort=t',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('U','http://www.radionl.fm/artiesten/?sort=u',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('V','http://www.radionl.fm/artiesten/?sort=v',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('W','http://www.radionl.fm/artiesten/?sort=w',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('X','http://www.radionl.fm/artiesten/?sort=x',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Y','http://www.radionl.fm/artiesten/?sort=y',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Z','http://www.radionl.fm/artiesten/?sort=z',250,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListArtist(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<div class="artistBox.*?">.*?<img src="(.*?)".*?<div class="name"><a href="(.*?)" title="">(.*?)</a>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for img, url, artist in match:
        img = 'http://radionl.fm' + img
        url = 'http://www.radionl.fm' + url
        utils.addDir(artist, url, 251, img, fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListSong(name, url, iconimage):
    listhtml = utils.getHtml2(url)
    match = re.compile('<div class="titel"><div class="titel_naam">(.*?)</div>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for song in match:
        url = name + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(song, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/artiesten.png', '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListSearch(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('value":"(.*?)"', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for artist in match:
        url = 'http://www.radionl.fm/artiesten/' + artist.replace(' ','-').replace('\/','/')
        name = artist.replace('\/','/')
        utils.addDir(name, url, 251, 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/hart-voor-muziek.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
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