import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import YDStreamExtractor 

# 130: vuurwerkfilmpjes.Main()
# 131: vuurwerkfilmpjes.Nieuw(url)
# 132: vuurwerkfilmpjes.Vuurwerkshows()
# 133: vuurwerkfilmpjes.Knalvuurwerk()
# 134: vuurwerkfilmpjes.Siervuurwerk()
# 135: vuurwerkfilmpjes.Merken1()
# 136: vuurwerkfilmpjes.Merken2()
# 137: vuurwerkfilmpjes.Lesli(url)
# 138: vuurwerkfilmpjes.Vuurwerkmania(url)
# 139: vuurwerkfilmpjes.Vuurwerkvisie(url)
# 140: vuurwerkfilmpjes.Wolff(url)
# 141: vuurwerkfilmpjes.Zena(url)
# 142: vuurwerkfilmpjes.Overige()
# 143: vuurwerkfilmpjes.Videos(url)
# 144: vuurwerkfilmpjes.Playvid(url, name)
# 145: vuurwerkfilmpjes.Search(url)

def Main():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Zoeken','http://www.vuurwerkfilmpjes.nl/?s=',145,icon)
    utils.addDir('Nieuwste Video\'s','http://www.vuurwerkfilmpjes.nl/',131,icon)
    utils.addDir('Vuurwerkshows','',132,icon)
    utils.addDir('Knalvuurwerk','',133,icon)
    utils.addDir('Siervuurwerk','',134,icon)
    utils.addDir('Merken A-K','',135,icon)
    utils.addDir('Merken L-Z','',136,icon)
    utils.addDir('Overig Vuurwerk','',142,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Nieuw(url):
    listhtml = utils.getHtml(url,url)
    matchtotaal = re.compile("Nieuwste Vuurwerkfilmpjes(.*?)<!-- /#carousel-->", re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('a title="(.*?)" href="(.*?)">.*?src="(.*?)".*?date">(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    for name, videopage, img, datum in match:
        name = utils.cleantext(name)
        name = name + ' (' + datum + ')'
        utils.addDir(name,videopage,144,img,Folder=False)
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Vuurwerkshows():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Nederland','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkshows-nederland/',143,icon)
    utils.addDir('Belgie','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkshows-belgie/',143,icon)
    utils.addDir('Duitsland','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkshow-duitsland/',143,icon)
    utils.addDir('Italie','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkshow-italie/',143,icon)
    utils.addDir('Spanje','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkshows-spanje/',143,icon)
    utils.addDir('Overige','http://www.vuurwerkfilmpjes.nl/categories/overige-vuurwerkshows/',143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Knalvuurwerk():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Losse Knallers','http://www.vuurwerkfilmpjes.nl/categories/illegaal-legaal-knalvuurwerk/',143,icon)
    utils.addDir('Knal Cakes','http://www.vuurwerkfilmpjes.nl/categories/knal-cakes-vuurwerk/',143,icon)
    utils.addDir('Matten & Rollen','http://www.vuurwerkfilmpjes.nl/categories/matten-rollen-vuurwerk/',143,icon)
    utils.addDir('Salute Shells','http://www.vuurwerkfilmpjes.nl/categories/salute-shells-vuurwerk-mortier/',143,icon)
    utils.addDir('Single Shots & Vuurpijlen','http://www.vuurwerkfilmpjes.nl/categories/single-shots-vuurpijlen-vuurwerk/',143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Siervuurwerk():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Professionele Cakes','http://www.vuurwerkfilmpjes.nl/categories/professionele-siervuurwerk-cakes/',143,icon)
    utils.addDir('Sier Shells','http://www.vuurwerkfilmpjes.nl/categories/sier-shells-vuurwerk-mortier/',143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Merken1():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Broekhoff','http://www.vuurwerkfilmpjes.nl/categories/broekhoff-vuurwerk/',143,icon)
    utils.addDir('Cafferata','http://www.vuurwerkfilmpjes.nl/categories/cafferata-vuurwerk/',143,icon)
    utils.addDir('China Red','http://www.vuurwerkfilmpjes.nl/categories/china-red-vuurwerk/',143,icon)
    utils.addDir('Dutch Dragon Fireworks','http://www.vuurwerkfilmpjes.nl/categories/dutch-dragon-fireworks-vuurwerk/',143,icon)
    utils.addDir('Evolution Fireworks','http://www.vuurwerkfilmpjes.nl/categories/evolution-fireworks/',143,icon)
    utils.addDir('GBV - Weco','http://www.vuurwerkfilmpjes.nl/categories/gbv-weco-vuurwerk/',143,icon)
    utils.addDir('Katan Vuurwerk','http://www.vuurwerkfilmpjes.nl/categories/katan-vuurwerk/',143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Merken2():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Lesli Vuurwerk','http://www.vuurwerkfilmpjes.nl/categories/lesli-vuurwerk/',137,icon)
    utils.addDir('Royal Fireworks','http://www.vuurwerkfilmpjes.nl/categories/royal-fireworks/',143,icon)
    utils.addDir('Rubro Vuurwerk','http://www.vuurwerkfilmpjes.nl/categories/rubro-vuurwerk/',143,icon)
    utils.addDir('Vulcan Europe','http://www.vuurwerkfilmpjes.nl/categories/vulcan-europe/',143,icon)
    utils.addDir('Vuurwerkmania','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkmania-vuurwerk/',138,icon)
    utils.addDir('Vuurwerkvisie','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkvisie-vuurwerk/',139,icon)
    utils.addDir('Wolff Vuurwerk','http://www.vuurwerkfilmpjes.nl/categories/wolff-vuurwerk/',140,icon)
    utils.addDir('Zena Nederland','http://www.vuurwerkfilmpjes.nl/categories/zena-vuurwerk-nederland/',141,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Lesli(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Alles Lesli','http://www.vuurwerkfilmpjes.nl/categories/lesli-vuurwerk/',143,icon)
    listhtml = utils.getHtml(url,url)
    leslitotaal = re.compile('<a href="http://www.vuurwerkfilmpjes.nl/categories/lesli-vuurwerk/">Lesli Vuurwerk</a>(.*?)</ul>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<a href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(leslitotaal)
    for videospage, name in match:
        name = utils.cleantext(name)
        name = name
        utils.addDir(name,videospage,143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Vuurwerkmania(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    listhtml = utils.getHtml(url,url)
    vuurwerkmaniatotaal = re.compile('<a href="http://www.vuurwerkfilmpjes.nl/categories/vuurwerkmania-vuurwerk/">VuurwerkMania</a>.*?<ul class="dropdown-menu">(.*?)</ul>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<a href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(vuurwerkmaniatotaal)
    for videospage, name in match:
        name = utils.cleantext(name)
        name = name
        utils.addDir(name,videospage,143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Vuurwerkvisie(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    listhtml = utils.getHtml(url,url)
    vuurwerkvisietotaal = re.compile('<a href="http://www.vuurwerkfilmpjes.nl/categories/vuurwerkvisie-vuurwerk/">VuurwerkVisie</a>.*?<ul class="dropdown-menu">(.*?)</ul>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<a href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(vuurwerkvisietotaal)
    for videospage, name in match:
        name = utils.cleantext(name)
        name = name
        utils.addDir(name,videospage,143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Wolff(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Alles Wolff Vuurwerk','http://www.vuurwerkfilmpjes.nl/categories/wolff-vuurwerk/',143,icon)
    listhtml = utils.getHtml(url,url)
    wolfftotaal = re.compile('<a href="http://www.vuurwerkfilmpjes.nl/categories/wolff-vuurwerk/">Wolff Vuurwerk</a>.*?<ul class="dropdown-menu">(.*?)</ul>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<a href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(wolfftotaal)
    for videospage, name in match:
        name = utils.cleantext(name)
        name = name
        utils.addDir(name,videospage,143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Zena(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    listhtml = utils.getHtml(url,url)
    zenatotaal = re.compile('<a href="http://www.vuurwerkfilmpjes.nl/categories/zena-vuurwerk-nederland/">Zena Nederland</a>.*?<ul class="dropdown-menu">(.*?)</ul>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<a href="(.*?)">(.*?)</a></li>', re.IGNORECASE | re.DOTALL).findall(zenatotaal)
    for videospage, name in match:
        name = utils.cleantext(name)
        name = name
        utils.addDir(name,videospage,143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Overige():
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('Onze Eigen Vuurwerkfilmpjes','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkfilmpje-youtube/',143,icon)
    utils.addDir('Oud en Nieuw','http://www.vuurwerkfilmpjes.nl/categories/oud-en-nieuw-vuurwerk/',143,icon)
    utils.addDir('Vuurwerk In Het Voetbal','http://www.vuurwerkfilmpjes.nl/categories/vuurwerk-in-het-voetbal/',143,icon)
    utils.addDir('Vuurwerk Dichtbij','http://www.vuurwerkfilmpjes.nl/categories/vuurwerk-dichtbij/',143,icon)
    utils.addDir('Vuurwerk Van Vroeger','http://www.vuurwerkfilmpjes.nl/categories/vuurwerkmania-vuurwerk/',143,icon)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Videos(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    listhtml = utils.getHtml(url,url)
    match = re.compile('<div class="col-sm-4 col-xs-6 item responsive-height">.*?<a href="(.*?)".*?src="(.*?)".*?<h3>.*?">(.*?)</a>.*?date">(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, img, name, datum in match:
        name = utils.cleantext(name)
        name = name + ' (' + datum + ')'
        utils.addDir(name,videopage,144,img,Folder=False)
    try:
        nextp = re.compile('<a class="next page-numbers" href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        utils.addDir('Volgende pagina',nextp,143,icon)
    except:
        pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Playvid(url, name):
    dp = xbmcgui.DialogProgress()
    dp.create("Vuurwerk TV","Een ogenblik geduld.") 
    listhtml = utils.getHtml(url,url)
    matchtotaal = re.compile('<div class="player.*?">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    if 'www.youtube.com' in matchtotaal:
        match = re.compile('src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    elif 'vimeo.com' in matchtotaal:
        match = re.compile('iframe src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    if match:
        stream = YDStreamExtractor.getVideoInfo(match[0])
        if stream:
            videourl = stream.streamURL()
            dp.close()
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
    else:
        dp.close()
        utils.notify('Er zijn geen video\'s gevonden.')
        
        
def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','+')
    searchUrl = searchUrl + title
    page = page=None
    print "Searching URL: " + searchUrl
    Zoekresultaat(searchUrl)
    
def Zoekresultaat(url):
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    listhtml = utils.getHtml(url,url)
    match = re.compile('<div class="col-sm-4 col-xs-6 item responsive-height">.*?<a title="(.*?)" href="(.*?)".*?src="(.*?)".*?date">(.*?)</span>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name, videopage, img, datum in match:
        name = utils.cleantext(name)
        name = name + ' (' + datum + ')'
        utils.addDir(name,videopage,144,img,Folder=False)
    try:
        nextp = re.compile('<a class="next page-numbers" href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        utils.addDir('Volgende pagina',nextp,146,icon)
    except:
        pass
    xbmcplugin.endOfDirectory(utils.addon_handle)