import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('1500 - 1401','http://www.radionl.fm/top1500/?t1500Page=0',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('1400 - 1301','http://www.radionl.fm/top1500/?t1500Page=1',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('1300 - 1201','http://www.radionl.fm/top1500/?t1500Page=2',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('1200 - 1101','http://www.radionl.fm/top1500/?t1500Page=3',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('1100 - 1001','http://www.radionl.fm/top1500/?t1500Page=4',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('1000 - 901','http://www.radionl.fm/top1500/?t1500Page=5',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('900 - 801','http://www.radionl.fm/top1500/?t1500Page=6',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('800 - 701','http://www.radionl.fm/top1500/?t1500Page=7',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('700 - 601','http://www.radionl.fm/top1500/?t1500Page=8',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('600 - 501','http://www.radionl.fm/top1500/?t1500Page=9',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('500 - 401','http://www.radionl.fm/top1500/?t1500Page=10',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('400 - 301','http://www.radionl.fm/top1500/?t1500Page=11',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('300 - 201','http://www.radionl.fm/top1500/?t1500Page=12',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('200 - 101','http://www.radionl.fm/top1500/?t1500Page=13',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('100 - 1','http://www.radionl.fm/top1500/?t1500Page=14',241,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<td id="nr">(.+?)</td><td id="titelartiest"><p class="artiest">(.+?)</p><p class="titel">(.+?)</p>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for nummer, artist, song in match:
        name = nummer + '. ' + artist + ' - ' + song
        url = artist + ' ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-top-1500.png', '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    

    