import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import YDStreamExtractor 

def Main():
    utils.addDir('Aftellen naar 2017','http://forum.vuurwerkcrew.nl/forumdisplay.php?480-Aftellen-naar-2017',129,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    utils.addDir('Aftellen Archief (2005 - 2016)','http://forum.vuurwerkcrew.nl/forumdisplay.php?455-Films-O-amp-N-2005-2016',129,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def filmpjes(url):
    dp = xbmcgui.DialogProgress()
    count = 0
    dp.create("Vuurwerk TV","Laden van de video's")
    listhtml = utils.getHtml(url,url)
    match = re.compile('<a class="title" href="(.*?)" id=".*?">.*?</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for topicurl in match:
        topicurl = 'http://forum.vuurwerkcrew.nl/' + topicurl
        topichtml = utils.getHtml(topicurl,topicurl)
        youtube1 = re.compile('iframe.*?src=".*?youtube.com(.*?)".*?</iframe>', re.IGNORECASE | re.DOTALL).findall(topichtml)
        for videopage in youtube1:
            videopage = 'http://www.youtube.com' + videopage
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)
                
        youtube2 = re.compile('<a href="(.*?)" title="View this video at YouTube in a new window or tab" target="_blank">YouTube Video</a>', re.IGNORECASE).findall(topichtml)
        for videopage in youtube2:
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)    
                
        vimeo = re.compile('<embed width=".*?vimeo.com.*?id=(.*?)"', re.IGNORECASE | re.DOTALL).findall(topichtml)
        for videopage in vimeo:
            videopage = 'https://vimeo.com/' + videopage
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)   
        #dp.update(500)
        count = count + 5
        dp.update(count)
        xbmc.sleep(500)
    dp.close()
    
                
    try:
        nextptotaal = re.compile('<li class="navbit lastnavbit"><span>.*?</span></li>(.*?)hreadlist_controls toolsmen', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        nextp = re.compile('span class="prev_next"><a rel="next" href="(.*?)" title="(.*?)">', re.IGNORECASE | re.DOTALL).findall(nextptotaal)
        for nextpage, nexttitle in nextp:
            nextpage = 'http://forum.vuurwerkcrew.nl/' + nextpage
            utils.addDir(nexttitle,nextpage,129,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    except:
        pass
    xbmcplugin.endOfDirectory(utils.addon_handle)