import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Main():
    utils.addDir('Zoeken','http://www.ziggosporttotaal.nl/zoeken.html?s=',235,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/zst.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Laatste video','http://www.ziggosporttotaal.nl/video/?sort=recent',233,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/zst.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Meest bekeken','http://www.ziggosporttotaal.nl/video/?sort=most',233,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/zst.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Voetbal','http://www.ziggosporttotaal.nl/video/1-voetbal/',233,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/zst.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg') 
    utils.addDir('Racing','http://www.ziggosporttotaal.nl/video/22-racing/',233,'https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/zst.png','',fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<div class="video-list-item">.*?<a href="(.*?)">.*?img src="(.*?)".*?<span class="title">(.*?)</span>.*?<small class="date">(.*?)</small>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, datum in match:
        name = utils.cleantext(name) + ' - ' + datum
        videopage = "http://www.ziggosporttotaal.nl" + videopage
        img = "http://www.ziggosporttotaal.nl" + img
        utils.addDownLink(name, videopage, 236, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    try:
        nextp=re.compile('href="([^"]+)" class="nav-link icon-chevron-right"', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://www.ziggosporttotaal.nl" + nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 233,'', '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def SearchList(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<li class="video-list-item">.*?<a href="(.*?)" class="imgLink">.*?srcset="(.*?) 2x.*?<span class="video-title">(.*?)</span>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name in match:
        name = utils.cleantext(name)
        videopage = "http://www.ziggosporttotaal.nl" + videopage
        img = "http://www.ziggosporttotaal.nl" + img
        utils.addDownLink(name, videopage, 236, img, '', fanart='https://raw.githubusercontent.com/doki1/repo/master/NLView%20XML/fanart.jpg')
    try:
        nextp=re.compile(r'nav-link active">\d+<.*?href="([^"]+)" class="nav-link', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://www.ziggosporttotaal.nl/zoeken.html" + nextp.replace("&amp;","&").replace(" ","+")
        utils.addDir('Volgende Pagina', next, 234,'', '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile(r"file: '(.*?)'").findall(listhtml)
    if match:
        videourl = match[0]
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
        utils.notify('Oh oh','Couldn\'t find a playable video link')

def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','+')
    searchUrl = searchUrl + title
    print "Searching URL: " + searchUrl
    SearchList(searchUrl)