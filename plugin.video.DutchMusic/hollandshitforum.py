import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Programma Gemist','http://www.hollandsehitsforum.nl/index.php?option=com_content&view=category&layout=blog&id=168&Itemid=40',221,os.path.join(utils.imgDir, 'tvoranje.png'),'')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml(url, '')
    xbmc.log(listhtml)
    match = re.compile('<p style="text-align: center;" align="center"><b><span style="color: #004d86;">N I E U W</span></b></p>(.*?)<p style="text-align: center;" align="center"><b><span style="font-size: 9pt; color: #004d86;">Releases aanmelden:</span></b></p>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match1 = re.compile(r'<td[^<]+<p><b><span[^>]+>(\d.*?)</span>.*?width: 138.9pt.*?;">(.*?)</span>.*?<td style="width: 5cm;.*?<span[^>]+>(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(match)
    for datum, artiest, song in match1:
        name = utils.cleantext(datum) + ': ' + utils.cleantext(artiest) + ' - ' + utils.cleantext(song)
        url = artiest + ' - ' + song
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
        utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/HHF.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

