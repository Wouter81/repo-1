import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Top20','http://sterren.avrotros.nl/programma-s/radio-pips/sterrennl-top-20/de-lijst/',239,'','')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile('<div class="block-content item(.*?)severalweeks', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for lijst in match:
        try: 
            videopage = re.compile("javascript:window\.open\('(.*)','_self'\)", re.DOTALL | re.IGNORECASE).findall(lijst)[0]
            videopage = "http://sterren.avrotros.nl/" + videopage
        except: 
            videopage = url
        if  'no-video' in lijst:
            match1 = re.compile('<span class="top20-item-position">(.+?)</span>.*?<h3 class="top20-item-artist">(.+?)</h3>.*?<p class="body-text">(.+?)</p>', re.DOTALL | re.IGNORECASE).findall(lijst)
            for nummer, artist, song in match1:
                name = nummer + '. ' + artist.replace("&amp;","&").replace("&#039;","'").replace("&quot;"," ") + ' - ' + song.replace("&amp;","&").replace("&#039;","'").replace("&quot;"," ")
                url = artist + ' ' + song
                url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
                utils.addDir(name, url, '', os.path.join(utils.imgDir, 'sterren-nl-top20.png'), '')
        else:
            match1 = re.compile('<span class="top20-item-position">(.+?)</span>.*?<h3 class="top20-item-artist">(.+?)</h3>.*?<p class="body-text">(.+?)</p>', re.DOTALL | re.IGNORECASE).findall(lijst)
            for nummer, artist, song in match1:
                name = nummer + '. ' + artist.replace("&amp;","&").replace("&#039;","'").replace("&quot;"," ") + ' - ' + song.replace("&amp;","&").replace("&#039;","'").replace("&quot;"," ")
                utils.addDownLink(name, videopage, 231, os.path.join(utils.imgDir, 'sterren-nl-top20.png'), '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
