import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon, json

import utils


def Main():
    utils.addDir('Beste Zangers','http://www.npo.nl/beste-zangers/AT_2033328/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',231,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Sterren NL Muziekfeest','http://www.npo.nl/sterren-muziekfeest-op-het-plein/POMS_S_TROS_098898/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Sterren NL Top 20','http://www.npo.nl/sterren-nl-top-20/AT_2044447/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    utils.addDir('Sterren NL Specials','http://www.npo.nl/sterren-nl-special/AT_2048249/search?media_type=broadcast&start_date=&end_date=&start=0&rows=999999999',230,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/sterren-nl.png',fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def ListNpoGemist(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<a href=".*?\d{4}/([^"]+)">.*?//(.*?)&quot;.*?<h4>\s+(.*?)\s+<span.*?<h5>([^<]+)</h5>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, datum in match:
        name = datum + ' - Beste Zangers: ' + name
        img = "http://" + img
        utils.addDownLink(name, videopage, 232, img, '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListNpoGemist2(url):
    listhtml = utils.getHtml2(url)
    match = re.compile(r'<a href=".*?\d{4}/([^"]+)">.*?//(.*?)&quot;.*?<h4>\s+(.*?)\s+<span.*?<h5>([^<]+)</h5>', re.DOTALL | re.IGNORECASE).findall(listhtml)
    for videopage, img, name, datum in match:
        name = datum + ' - ' + name
        img = "http://" + img
        utils.addDownLink(name, videopage, 232, img, '', fanart='https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.DutchMusic/fanart.JPG')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def getJsContent(url):
    jslink = "http://e.omroep.nl/metadata/" + url
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