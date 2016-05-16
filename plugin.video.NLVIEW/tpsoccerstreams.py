import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Voetbal','http://www.tpsoccer.net/',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/tp.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r"<i class='fa fa-desktop'></i> (.*?)</a></li>", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for name in match:
        videopage = 'http://www.tpsoccer.net/p/' + name + '.html'
        name = 'Stream ' + name
        videopage = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + urllib.quote_plus(videopage)
        utils.addDownLink(name, videopage, 300, 'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/tp.png', '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)