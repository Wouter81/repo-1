import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3

import re,urlparse,json
from liveresolver.modules import client
from BeautifulSoup import BeautifulSoup as bs
import xbmcgui


def Main():
    utils.addDir('Samenvattingen Zoeken','http://footyroom.com/?q=',225,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Laatste Samenvattingen','http://footyroom.com/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Eredivisie (Nederland)','http://footyroom.com/videos/holland/eredivisie/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('KNVB Beker (Nederland)','http://footyroom.com/videos/holland/knvb-cup/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Barclays Premier League (Engeland)','http://footyroom.com/videos/england/premierleague/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('FA Cup (Engeland)','http://footyroom.com/videos/england/facup/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Capital One Cup (Engeland)','http://footyroom.com/videos/england/carlingcup/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Serie A (Italie)','http://footyroom.com/videos/italy/seriea/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Coppa Italia (Italie)','http://footyroom.com/videos/italy/coppaitalia/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Ligue 1 (Frankrijk)','http://footyroom.com/videos/france/ligue1/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Coupe de la Ligue (Frankrijk)','http://footyroom.com/videos/france/coupe-de-la-ligue/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Coupe de France (Frankrijk)','http://footyroom.com/videos/france/coupe-de-france/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('La Liga (Spanje)','http://footyroom.com/videos/spain/laliga/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Copa del Rey (Spanje)','http://footyroom.com/videos/spain/copadelrey/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Bundesliga (Duitsland)','http://footyroom.com/videos/germany/bundesliga/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('DFB Pokal (Duitsland)','http://footyroom.com/videos/germany/dfbpokal/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Primeira Liga (Portugal)','http://footyroom.com/videos/portugal/liga-sagres/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Taca de Portugal (Portugal)','http://footyroom.com/videos/portugal/taca-de-portugal/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Super Lig (Turkije)','http://footyroom.com/videos/turkey/super-lig/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Turkish Cup (Turkije)','http://footyroom.com/videos/turkey/turkish-cup/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Premier League (Rusland)','http://footyroom.com/videos/russia/russianpremierleague/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Major League Soccer (USA)','http://footyroom.com/videos/usa/mls/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Champions League','http://footyroom.com/videos/europe/uefachampionsleague/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League','http://footyroom.com/videos/europe/uefaeuropaleague/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Internationaal Vriendschapelijk','http://footyroom.com/videos/international/friendly/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Clubs Vriendschapelijk','http://footyroom.com/videos/germany/dfbpokal/',224,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/samenvatting.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<div class="vid ">.*?<header class="vidTop"><a href="(.*?)" target="_blank">(.*?)</a></header>.*?<img src="(.*?)" />', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, name, img in match:
        videopage = "http://footyroom.com" + videopage
        utils.addDownLink(name, videopage, 226, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
#    try:
#        page = page + 1
#        nextp=re.compile('href="([^"]+)"> Vol', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
#        next = "http://www.tvoranje.nl" + nextp.replace("&amp;","&")
#        utils.addDir('Volgende Pagina', next, 224,'', page)
#    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Playvid(url, name):
    import YDStreamExtractor
    vid = YDStreamExtractor.getVideoInfo(url,quality=1)
    stream_url = vid.streamURL()
    if stream_url:
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Sport'})
        listitem.setProperty("IsPlayable","true")
        if int(sys.argv[1]) == -1:
            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            pl.clear()
            pl.add(stream_url, listitem)
            xbmc.Player().play(pl)
        else:
            listitem.setPath(str(stream_url))
            xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)        
        

def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','%20')
    searchUrl = searchUrl + title
    print "Searching URL: " + searchUrl
    List(searchUrl)

