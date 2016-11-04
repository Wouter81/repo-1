import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main(): 
    #utils.addDir('Zoeken','',998,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    #utils.addDir('','',105,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg', Folder=False)   
    utils.addDir('[B]Nederlands vuurwerk[/B]','',105,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg', Folder=False) 
    listhtmlnl = utils.getHtml('http://forum.vuurwerkcrew.nl/forumdisplay.php?172-Nederlands-vuurwerk','http://forum.vuurwerkcrew.nl/')
    matchnl = re.compile('<li id=".*?" class="forumbit_post old L1">.*?<h2 class="forumtitle"><a href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtmlnl)
    for forumpage, name in matchnl:
        name = utils.cleantext(name)
        if 'Siervuurwerk algemeen' in name:
            pass
        elif 'Knalvuurwerk & Klein vuurwerk' in name:
            pass
        elif 'Vuurwerkwinkels Nederland' in name:
            pass
        elif 'De Antiekhoek' in name:
            pass
        elif 'Archief' in name:
            pass
        else:
            forumpage = 'http://forum.vuurwerkcrew.nl/' + forumpage
            utils.addDir(name,forumpage,106,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    listhtmlint = utils.getHtml('http://forum.vuurwerkcrew.nl/forumdisplay.php?251-Buitenlands-vuurwerk','http://forum.vuurwerkcrew.nl/')
    utils.addDir('','',105,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg', Folder=False) 
    utils.addDir('[B]Buitenlands vuurwerk[/B]','',105,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg', Folder=False)
    matchint = re.compile('<li id=".*?" class="forumbit_post old L1">.*?<h2 class="forumtitle"><a href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtmlint)
    for forumpage, name in matchint:
        name = utils.cleantext(name)
        if 'Vuurwerkwinkels Buitenland' in name:
            pass
        else:
            forumpage = 'http://forum.vuurwerkcrew.nl/' + forumpage
            utils.addDir(name,forumpage,106,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml(url,'http://forum.vuurwerkcrew.nl/')
    match = re.compile('<li id=".*?" class="forumbit_post old L1">.*?<h2 class="forumtitle"><a href="(.*?)">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for forumpage, name in match:
        name = utils.cleantext(name)
        if 'Algemeen' in name:
            pass
        elif 'Archief' in name:
            pass
        elif 'Choo' in name:
            pass
        else:
            forumpage = 'http://forum.vuurwerkcrew.nl/' + forumpage
            utils.addDir(name,forumpage,107,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Listproducten(url):
    listhtml = utils.getHtml(url,'http://forum.vuurwerkcrew.nl/')
    match = re.compile('<div class="rating.*? nonsticky">.*?<a class="title" href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for productpage, name in match:
        name = utils.cleantext(name)
        productpage = 'http://forum.vuurwerkcrew.nl/' + productpage
        utils.addDir(name,productpage,108,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    try:
        nextptotaal = re.compile('<li class="navbit lastnavbit"><span>.*?</span></li>(.*?)hreadlist_controls toolsmen', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        nextp = re.compile('span class="prev_next"><a rel="next" href="(.*?)" title="(.*?)">', re.IGNORECASE | re.DOTALL).findall(nextptotaal)
        for nextpage, nexttitle in nextp:
            nextpage = 'http://forum.vuurwerkcrew.nl/' + nextpage
            utils.addDir(nexttitle,nextpage,107,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    except:
        pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Productpage(url):
    listhtml = utils.getHtml(url,'http://forum.vuurwerkcrew.nl/')
    try:
        postimage = re.compile('<div id="post_message_.*?">(.*?)<div class="after_content">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        img = re.compile('img src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(postimage)[0]
    except:
        img = 'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg'
    match = re.compile('DarkRed">(.*?)<br />', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name in match:
        name = utils.striphtml(name)
        name = utils.cleantext(name)
        name = name.replace('\n','').replace('\t','')
        if 'O.a te koop' in name:
            pass
        elif 'Foto' in name:
            pass
        elif 'O.a' in name:
            pass
        else:
            utils.addDir(name, '', 105, img, Folder=False)
    utils.addDir('','',105,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg', Folder=False)     
    try:
        youtube = re.compile(r'iframe.*?src=".*?youtube.com/embed/(.*?)\?wmode.*?</iframe>', re.IGNORECASE | re.DOTALL).findall(listhtml)
        for youtube in youtube:
            youtube = 'plugin://plugin.video.youtube/play/?video_id=' + youtube
            utils.addDownLink('Klik hier voor een video van Vuurwerkcrew', youtube, 300, img, '')
    except: pass
    
    lurl = re.compile("""<span class="first_last"><a href="([^"]+)" title="Laatste pagina""", re.IGNORECASE | re.DOTALL).findall(listhtml) 
    if lurl:
        laatstepagina = utils.getHtml('http://forum.vuurwerkcrew.nl/' + lurl[0], '')
        try: 
            youtube = re.compile(r'iframe.*?src=".*?youtube.com/embed/(.*?)\?wmode.*?</iframe>', re.IGNORECASE | re.DOTALL).findall(laatstepagina)
            for youtube in youtube:
                youtube = 'plugin://plugin.video.youtube/play/?video_id=' + youtube 
                utils.addDownLink('Klik hier voor een video van Vuurwerkcrew', youtube, 300, img, '') 
        except: pass 
    
    try:
        youtubezoeken = re.compile('<li class="navbit"><a href="forumdisplay.*?">.*?</a>./li>.*?href="forumdisplay.*?">(.*?)</a>.*?href="forumdisplay.*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
        for importeur, artikelnaam in youtubezoeken:
            name = artikelnaam + ' ' + importeur
            url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(name)
            utils.addDir('Bekijk meer video\'s', url, '', img, '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)