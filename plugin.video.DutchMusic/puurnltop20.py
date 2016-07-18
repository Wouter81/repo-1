import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def List(url, page=None):
    url = 'http://puurnl.fm/top20/'
    listhtml = utils.getHtml2(url)
    periode = re.compile('<div class="data">.?.?(.*?).?.?.?</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    utils.addDir('[B]Puur NL Top 20 ' + periode + ':[/B]', '', '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png', '')
    
    match = re.compile('nummer">(.*?) .*?</div><div class="titel"> (.*?) </div>.*?artiest"> (.*?) </div>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for nummer, song, artist in match:
        if '.' in artist:
            artist = artist.decode('latin1').encode('utf8')
            song = song.decode('latin1').encode('utf8')
            name = nummer + '. ' + artist + ' - ' + song
            url = song
            url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
            utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/puurnl-top20.png', '')
        else:
            artist = artist.decode('latin1').encode('utf8')
            song = song.decode('latin1').encode('utf8')            
            name = nummer + '. ' + artist + ' - ' + song
            url = artist + ' ' + song
            url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
            utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png', '')
    
    superschijf = re.compile('superschijf"><div class="titel"> (.*?) </div>.*?<div class="artiest"> (.*?)</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for song, artist in superschijf:
        artist = artist.decode('latin1').encode('utf8')
        song = song.decode('latin1').encode('utf8')        
        name = 'Puur NL Superschijf: ' + artist + ' - ' + song
        url = artist + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
    utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    

    