import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Programma Gemist','http://www.hollandsehitsforum.nl/index.php?option=com_content&view=category&layout=blog&id=168&Itemid=40',221,os.path.join(utils.imgDir, 'tvoranje.png'),'')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml(url, '')
    match = re.compile("RELEASES NIEUW(.*?)Releases aanmelden", re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match1 = re.compile("""<tr>.*?<p style="text-align: center;" align="center"><span style="font-size: 8pt; font-family: 'Arial','sans-serif';">(.*?)</span>.*?<p><span style="font-size: 8pt; font-family: 'Arial','sans-serif';">(.*?)</span>.*?<p><span style="font-size: 8pt; font-family: 'Arial','sans-serif';">(.*?)</span>""", re.IGNORECASE | re.DOTALL).findall(match)
    for datum, artiest, song in match1:
        if '&nbsp;' in song:
            pass
        else:   
            name = utils.cleantext(datum) + ': ' + utils.cleantext(artiest) + ' - ' + utils.cleantext(song)
            url = artiest + ' - ' + song
            #url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(url)
            url = 'plugin://plugin.video.youtube/search/?q=' + url
            xbmc.log(url)
            utils.addDir(name, url, '', 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/HHF.png', '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

