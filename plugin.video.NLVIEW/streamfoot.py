import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Voetbal','http://www.stream-foot.tv/index.php?streaming=Football',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Basketbal','http://www.stream-foot.tv/index.php?streaming=Basketball',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Rugby','http://www.stream-foot.tv/index.php?streaming=Rugby',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Formule 1','http://www.stream-foot.tv/index.php?streaming=Formule1',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Tennis','http://www.stream-foot.tv/index.php?streaming=Tennis',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Overige','http://www.stream-foot.tv/index.php?streaming=Tennis',241,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')   
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<li class="liProg">(.*?)</li>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for regel in match:
        if 'class="Day"' in regel:
            datum = re.compile('<p class="Day">([^<]+)</p>', re.DOTALL | re.IGNORECASE).findall(regel)[0]
            utils.addDir(datum, '', '', 'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png', Folder=False, fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
        match = re.compile(r'class="date">(.*?) :</span>.*?<a href="(.*?)" title=".*?">.*?\n(.*?):', re.DOTALL | re.IGNORECASE).findall(regel)
        for tijd, videopage, name in match:
            name = '[COLOR lime]' + tijd + ': [/COLOR]' + utils.cleantext(name)
            videopage = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + urllib.quote_plus(videopage)
            utils.addDownLink(name, videopage, 300, 'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/s-f.png', '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)