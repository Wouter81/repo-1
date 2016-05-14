import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Zoeken','http://www.foxsports.nl/search/videos/?q=',230,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Laatste Video','http://www.foxsports.nl/video/filter/fragments/1/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Samenvattingen','',237,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Doelpunten','',238,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Interviews','',239,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Analyses','http://www.foxsports.nl/video/filter/fragments/1/analyses/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Voetbal','http://www.foxsports.nl/video/filter/fragments/1/alle/voetbal/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Tennis','http://www.foxsports.nl/video/filter/fragments/1/alle/tennis/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Overige','http://www.foxsports.nl/video/filter/fragments/1/alle/overige/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Aanbevolen','http://www.foxsports.nl/video/filter/fragments/1/aanbevolen/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Meest bekeken','http://www.foxsports.nl/video/meest_bekeken/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Videoklasiekers','http://www.foxsports.nl/video/filter/fragments/1/videoklassiekers/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Meer','http://www.foxsports.nl/video/filter/fragments/1/meer_video/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def MainSamenvattingen():
    utils.addDir('Alle Samenvattingen','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Voetbal Samenvattingen','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Eredivisie','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/eredivisie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('Jupiler League','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/jupiler-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('KNVB Beker','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/knvb-beker/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/uefa-europa-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Barclays Premier League','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/barclays-premier-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('FA Cup','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/fa-cup/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('DFB Pokal','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/dfb-pokal/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/uefa-europa-league-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('EK Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/ek-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Tweede Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/samenvattingen/voetbal/tweede-bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def MainDoelpunten():
    utils.addDir('Alle Doelpunten','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Eredivisie','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/eredivisie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('Jupiler League','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/jupiler-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('KNVB Beker','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/knvb-beker/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/uefa-europa-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Barclays Premier League','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/barclays-premier-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('FA Cup','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/fa-cup/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('DFB Pokal','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/dfb-pokal/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/uefa-europa-league-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('EK Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/ek-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Tweede Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/doelpunten/voetbal/tweede-bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def MainInterviews():
    utils.addDir('Alle Doelpunten','http://www.foxsports.nl/video/filter/fragments/1/interviews/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Eredivisie','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/eredivisie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('Jupiler League','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/jupiler-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('KNVB Beker','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/knvb-beker/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/uefa-europa-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Barclays Premier League','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/barclays-premier-league/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')  
    utils.addDir('FA Cup','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/fa-cup/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('DFB Pokal','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/dfb-pokal/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('UEFA Europa League Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/uefa-europa-league-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('EK Kwalificatie','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/ek-kwalificatie/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    utils.addDir('Tweede Bundesliga','http://www.foxsports.nl/video/filter/fragments/1/interviews/voetbal/tweede-bundesliga/',228,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fs.png',1,fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile("""src='([^']+)' alt='([^<]+)'>.*?href="([^"]+)""", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for img, name, videopage in match:
        name = utils.cleantext(name)
        videopage = "http://www.foxsports.nl" + videopage
        utils.addDownLink(name, videopage, 231, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    if len(match) == 12:
        npage = page + 1        
        url = url.replace('/'+str(page)+'/','/'+str(npage)+'/')
        utils.addDir('Volgende Pagina ('+str(npage)+')', url, 228, '', npage)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def SearchList(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<article class="dcm-article">.*?<a href="(.*?)">.+?src="(.*?)".*?<a href=".*?">(.*?)</a>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name in match:
        name = utils.cleantext(name)
        utils.addDownLink(name, videopage, 231, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    try:
        nextp=re.compile(r'dcm-active">\d+<.*?href="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://www.foxsports.nl/video/search/" + nextp.replace("&amp;","&").replace(" ","%20")
        utils.addDir('Volgende Pagina', next, 229,'', '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    videoid = re.compile('data-videoid="(.*?)"', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    videoid = 'http://www.foxsports.nl/divadata/Output/VideoData/' + videoid + '.xml'
    videoxml = utils.getHtml2(videoid)
    videourl = re.compile(r'<uri>([^<]+m3u8)</uri>', re.DOTALL | re.IGNORECASE).findall(videoxml)[0]
    if videourl:
        iconimage = xbmc.getInfoImage("ListItem.Thumb")
        listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        listitem.setInfo('video', {'Title': name, 'Genre': 'Music'})
        listitem.setProperty("IsPlayable","true")
        if int(sys.argv[1]) == -1:
            pl = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
            pl.clear()
            pl.add(videourl, listitem)
            xbmc.Player().play(pl)
        else:
            listitem.setPath(str(videourl))
            xbmcplugin.setResolvedUrl(utils.addon_handle, True, listitem)

def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','%20')
    searchUrl = searchUrl + title + '&s=date'
    print "Searching URL: " + searchUrl
    SearchList(searchUrl)