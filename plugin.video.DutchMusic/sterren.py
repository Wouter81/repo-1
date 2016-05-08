import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, json

import utils


def Main():
    #utils.addDir('Zoeken','http://sterren.avrotros.nl/zoeken/?tx_solr%5Bq%5D=',233,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Nieuwste uitzendingen','http://sterren.avrotros.nl/video-s/meer-uitzendingen/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Nieuwste clips','http://sterren.avrotros.nl/video-s/nieuwe-videoclips-overzicht/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('De Zomer Voorbij','http://sterren.avrotros.nl/programma-s/tv-pips/de-zomer-voorbij/dezomervoorbij-tv-videos1/video-overzicht/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('De Winter Voorbij','http://sterren.avrotros.nl/programma-s/tv-pips/dewintervoorbij/dewintervoorbij-tv-videos/fragmenten/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Specials','http://sterren.avrotros.nl/video-s/video-specials/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('De Beste Zangers van Nederland','http://sterren.avrotros.nl/programma-s/tv-pips/de-beste-zangers-van-nl/debestezangersvannl-tv-videos/alle-video-s/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Sterrenparade clips','http://sterren.avrotros.nl/programma-s/tv-pips/sterrenparade/sterrenparade-tv-videos/overzicht-sterrenparade-clips/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    #utils.addDir('TROS Muziekfeest','http://sterren.avrotros.nl/programma-s/tv-pips/sterren-muziekfeest/sterrenmuziekfeest-tv-videos1/optredens-muziekfeest-op-het-plein/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Op Volle Toeren','http://sterren.avrotros.nl/video-s/meer-clips-op-volle-toeren/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')   
    utils.addDir('Mega Piraten Festijn','http://sterren.avrotros.nl/programma-s/tv-pips/mpf/mpf-tv-videos/mega-piratenfestijn-video-overzicht/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'')
    utils.addDir('Toppop','http://sterren.avrotros.nl/programma-s/tv-pips/toppop/toppop-tv-videos/overzicht/',230,os.path.join(utils.imgDir, 'sterren-nl.png'),'') 
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a class="rounded-img" href="(.+?)">.+?<img src="(.+?)" alt=".+?" />.+?<span class="video-item-title" title="(.+?)">.+?<span class="video-item-subtitle" title="(.+?)">', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, name2 in match:
        name = name + ' - ' + name2
        videopage = "http://sterren.avrotros.nl" + videopage
        utils.addDownLink(name, videopage, 231, img, '')
    try:
        page = page + 1
        nextp=re.compile('href="([^"]+)">Vol', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://sterren.avrotros.nl/" + nextp
        utils.addDir('Volgende Pagina', next, 230,'', page)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListSearch(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile('<li class="results-entry">(.*?)date', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for searchresult in match:
        try: img = re.compile('img src="([^"]+)"', re.DOTALL | re.IGNORECASE).findall(searchresult)[0]
        except: img = ""
        match1 = re.compile('<h3><a href="([^"]+)">([^<]+)<').findall(searchresult)
        videopage = match1[0][0]
        name = match1[0][1].replace("&amp;","&").replace("&#039;","'").replace("&quot;"," ")
        utils.addDownLink(name, videopage, 231, img, '')
    try:
        nextp=re.compile('<a href="(zoeken[^"]+)"><img src="/fileadmin/GFX/pagebrowser-button-next.png"', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://sterren.avrotros.nl/" + nextp.replace("&amp;","&").replace(" ","%20")
        utils.addDir('Volgende Pagina', next, 232,'', '')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def getJsContent(url):
    listhtml = utils.getHtml(url,'')
    jslink = re.compile("var currVideoId = '(.+?)';", re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
    jslink = "http://e.omroep.nl/metadata/" + jslink
    jscontent = utils.getHtml(jslink,'')
    return jscontent

def Playvid(url, name):
    i = 0
    while (i < 5):
        jscontent = getJsContent(url)
        i += 1
        if not 'ERROR' in jscontent:
            break
    if 'kwaliteit' in jscontent:
        match = re.compile('"kwaliteit":3,"url":"(.+?)"}', re.DOTALL | re.IGNORECASE).findall(jscontent)[0]
        if match:
            videourl = match.replace("\/","/")
    elif 'prid' in jscontent:
        match = re.compile('prid":"([^"]+)"', re.DOTALL | re.IGNORECASE).findall(jscontent)[0]
        if match:
            videourl = get_play_url(match)
    else:
        videourl = None
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
    else:
        utils.notify('Oh oh','Couldn\'t find a playable video link')
   
   
def get_play_url(whatson_id):
    ##token aanvragen
    data = utils.getHtml('http://ida.omroep.nl/npoplayer/i.js', '')
    token = re.compile('.token\s*=\s*"(.*?)"', re.DOTALL + re.IGNORECASE).search(str(data)).group(1)
    ##video lokatie aanvragen
    data = utils.getHtml('http://ida.omroep.nl/odi/?prid='+whatson_id+'&puboptions=adaptive&adaptive=yes&part=1&token='+__get_newtoken(token), '')
    json_data = json.loads(data)
    ##video file terug geven vanaf json antwoord
    streamdataurl = json_data['streams'][0]
    streamurl = str(streamdataurl.split("?")[0]) + '?extension=m3u8'
    data = utils.getHtml(streamurl, '')
    json_data = json.loads(data)
    url_play = json_data['url']
    return url_play

def __get_newtoken(token):
    # site change, token invalid, needs to be reordered. Thanks to rieter for figuring this out very quickly.
    first = -1
    last = -1
    for i in range(5, len(token) - 5, 1):	
        if token[i].isdigit():
            if first < 0:
                first = i                
            elif last < 0:
                last = i                
                break

    newtoken = list(token)
    if first < 0 or last < 0:
        first = 12
        last = 13
    newtoken[first] = token[last]
    newtoken[last] = token[first]
    newtoken = ''.join(newtoken)    
    return newtoken

def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','%20')
    searchUrl = searchUrl + title + '&tx_solr%5Bfilter%5D%5B0%5D=type%3AVideo'
    print "Searching URL: " + searchUrl
    ListSearch(searchUrl)