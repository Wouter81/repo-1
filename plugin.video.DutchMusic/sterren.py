import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, json

import utils


def Main():
    utils.addDir('Sterren NL Fragmenten','http://sterren-app.npo.nl/videos/page/1/',266,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Beste Zangers','http://www.npo.nl/beste-zangers/AT_2033328/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',231,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren NL Muziekfeest & Mega Piraten Festijn','http://www.npo.nl/sterren-muziekfeest-op-het-plein/AT_2033326/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren NL Top 20','http://www.npo.nl/sterren-nl-top-20/AT_2044447/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren NL Specials','http://www.npo.nl/sterren-nl-special/AT_2048249/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren NL Carnaval','http://www.npo.nl/sterren-nl-carnaval/POMS_S_TROS_123361/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren NL Awards','http://www.npo.nl/sterren-nl-awards/POMS_S_TROS_123349/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    utils.addDir('Sterren.nl Archief (Tot en met 2014)','http://www.npo.nl/sterren-nl/POMS_S_TROS_165497/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png')
    #utils.addDir('Sterren.nl Specials (tot december 2015)','http://www.npo.nl/sterren-nl-specials/POMS_S_TROS_123319/search?page=1&category=broadcasts',233,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png', 1)
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListNpoGemist(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<a href=".*?\d{4}/([^"]+)">.*?//(.*?)&quot;.*?<h4>\s+(.*?)\s+<span.*?<h5>([^<]+)</h5>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, datum in match:
        name = datum + ' - Beste Zangers: ' + name
        img = "http://" + img
        utils.addDownLink(name, videopage, 232, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListNpoGemist2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<a href=".*?\d{4}/([^"]+)">.*?//(.*?)&quot;.*?<h4>\s+(.*?)\s+<span.*?<h5>([^<]+)</h5>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, datum in match:
        name = datum + ' - ' + name
        img = "http://" + img
        utils.addDownLink(name, videopage, 232, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListNpoGemist3(url, page=None):
    listhtml = utils.getHtml2(url)
    match = re.compile('src="//(.*?)".*?href="/(.*?)">(.*?)</a>.*?</span> (.*?)</h4>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for img, videopage, name, datum in match:
        name = utils.cleantext(datum) + ' - ' + utils.cleantext(name)
        img = "http://" + img
        videopage = "http://www.npo.nl" + videopage
        utils.addDownLink(name, videopage, 232, img, '')
    if len(match) <= 5:
        npage = page + 1        
        url = url.replace('page='+str(page)+'&c','page='+str(npage)+'&c')
        utils.addDir('Volgende Pagina ('+str(npage)+')', url, 233, '', npage)
    xbmcplugin.endOfDirectory(utils.addon_handle)

def ListSterrenVideos(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a href="([^"]+)" class="teaser-link" title="([^"]+)".*?src="([^"]+)".*?<span[^>]+>([^<]+)</span>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, name, img, datum in match:
        name = datum.strip() + ' - ' + name.replace('&amp;','&')
        videopage = 'http://sterren-app.npo.nl/' + videopage
        img = "http://sterren-app.npo.nl/" + img
        utils.addDownLink(name, videopage, 267, img, '')
    try:
        nextp=re.compile('Volgende" href="(.*?)"', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        next = "http://sterren-app.npo.nl" + nextp.replace("&amp;","&")
        utils.addDir('Volgende Pagina', next, 266,'')
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)

def getJsContent(url):
    jslink = "http://e.omroep.nl/metadata/" + url
    jscontent = utils.getHtml(jslink,'')
    return jscontent

def Playvid(url, name):
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")  
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

def PlayvidSterren(url, name):
    listhtml = utils.getHtml2(url)
    match = re.compile('embed/([^\?]+)', re.IGNORECASE | re.DOTALL).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")  
    if match:
        videourl = match[0]
        videourl = 'plugin://plugin.video.youtube/play/?video_id=' + urllib.quote_plus(videourl)
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