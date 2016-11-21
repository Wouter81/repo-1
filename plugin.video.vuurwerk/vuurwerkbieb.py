import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import YDStreamExtractor 


def Main():
    utils.addDir('Zoeken','http://www.vuurwerkbieb.nl/index.php/zoekresultaten?z=',117,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Bekijk alle producten','http://www.vuurwerkbieb.nl/zoekresultaten/?volg=0/?all=yes',115,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Sorteren op importeur','http://www.vuurwerkbieb.nl/zoekresultaten/?volg=0/?all=yes',110,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Sorteren op soort vuurwerk','http://www.vuurwerkbieb.nl/zoekresultaten/?volg=0/?all=yes',114,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')    
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Listimporteur(url):
    listhtml = utils.getHtml2(url)
    matchtotaal = re.compile('</div-->Merken(.*?)<input type="hidden" id="filterimporteurs" value="" /><script language="javascript">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<input type="checkbox" id=".*?" name="iID" value="(.*?)".*?</span>(.*?)</label>', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    for id, name in match:
        listpage = 'http://www.vuurwerkbieb.nl/zoekresultaten/?volg=0/?all=yes&i=' + id
        name = utils.cleantext(name)
        utils.addDir(name,listpage,111,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Importeurmenu(name, url):
    utils.addDir('Bekijk alle producten van ' + name,url,115,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Sorteren op collectie',url,112,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Sorteren op soort vuurwerk',url,114,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Listcollectieimporteur(url):
    listhtml = utils.getHtml2(url)
    matchtotaal = re.compile('<div id="omfiltercollecties">(.*?)<script language="javascript">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<input type="checkbox" id=".*?" name="colID" value="(.*?)".*?</span>(.*?)</label>', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    for id, name in match:
        listpage = url + '&c=' + id
        name = utils.cleantext(name)
        utils.addDir(name,listpage,113,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Collectiemenu(name, url):
    utils.addDir('Bekijk alle producten van de ' + name + ' collectie',url,115,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Sorteren op soort vuurwerk',url,114,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ListSoortVuurwerk(url):
    listhtml = utils.getHtml2(url)
    matchtotaal = re.compile('div class="pijltje  vast" rel="vwb03"></div>(.*?)"hidden" id="filtersoorten" value="" /><script language="javascript">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<input type="checkbox" id=".*?" name="SID" value="(.*?)".*?</span>(.*?)</label>', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
    for id, name in match:
        listpage = url + '&s=' + id
        name = utils.cleantext(name)
        utils.addDir(name,listpage,115,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
#def ListSoortVuurwerk(url):
#    listhtml = utils.getHtml2(url)
#    matchtotaal = re.compile(r'Selecteer hier welke vuurwerksoorten u alleen wilt zien(.*?)<script language="javascript">//\$\(document\)\.ready\(function\(\){', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
#    match = re.compile('<input type="checkbox" id=".*?" name="SID" value="(.*?)".*?</span>(.*?)</label>', re.IGNORECASE | re.DOTALL).findall(matchtotaal)
#    for id, name in match:
#        listpage = url + '&s=' + id
#        name = utils.cleantext(name)
#        utils.addDir(name,listpage,115,'https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg')
#    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Productlist(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('<a href="http://www.vuurwerkbieb.nl(.*?)".*?src="(.*?)".*?h3>(.*?)</h3>.*?Artikelnummer: (.*?)<br />.*?">(.*?)</span>').findall(listhtml)
    for productpage, img, name, artikelnummer, merk in match:
        artikelnummer = utils.cleantext(artikelnummer)
        name = artikelnummer + ': ' + name + ' (' + merk + ')'
        productpage = 'http://www.vuurwerkbieb.nl' + productpage
        img = 'http://www.vuurwerkbieb.nl' + img
        utils.addDir(name,productpage,116,img)
    if len(match) == 100:
        page = 0
        npage = page + 1
        url = url.replace('/?volg='+str(page)+'/','/?volg='+str(npage)+'/')
        xbmc.log(url)
        utils.addDir('Volgende Pagina ('+str(npage)+')', url, 999, '', npage)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def ProductlistNext(url, page=None):
    listhtml = utils.getHtml2(url)
    matchtotaal = re.compile('Naar vorige pagina" /></span></a></div>(.*?)volgendepagina', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('href="(.*?)".*?src="(.*?)".*?h3>(.*?)</h3>.*?Artikelnummer: (.*?)<br />.*?merk">(.*?)</span>').findall(matchtotaal)
    for productpage, img, name, artikelnummer, merk in match:
        artikelnummer = utils.cleantext(artikelnummer)
        name = artikelnummer + ': ' + name + ' (' + merk + ')'
        img = 'http://www.vuurwerkbieb.nl' + img
        utils.addDir(name,productpage,116,img)
    if len(match) == 100:
        npage = page + 1        
        url = url.replace('?volg='+str(page)+'/','?volg='+str(npage)+'/')
        xbmc.log(url)
        utils.addDir('Volgende Pagina ('+str(npage)+')', url, 999, '', npage)
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Productpagina(url):
    dp = xbmcgui.DialogProgress()
    dp.create("Vuurwerk TV","Laden van de productinformatie en video's.")
    listhtml = utils.getHtml2(url)
    image = re.compile('<div class="image">.*?href="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<div class="attr.*?">(.*?)</div>.*?<div class="spec.*?">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name1, name2 in match:
        name1 = utils.striphtml(name1)
        name2 = utils.striphtml(name2)
        name1 = utils.cleantext(name1)
        name2 = utils.cleantext(name2)
        name = '[B]' + name1 + ' [/B]' + name2
        if 'Website merk:' in name:
            pass
        else:
            utils.addDir(name,'',116,image)

    prijs = re.compile('<h3>(.*?)</h3>.*?omrij">.*?">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for eerste, tweede in prijs:
        if 'Menu' in eerste:
            pass
        elif 'Technische Specificaties' in eerste:
            pass
        elif 'Gewichten' in eerste:
            pass
        elif 'Effectomschrijving' in eerste:
            pass
        else:
            tweede = utils.cleantext(tweede)
            utils.addDir('[B]' + eerste + ': [/B]' + tweede,'',116,image)
    utils.addDir('','',116,image)
    try:
        matchyoutube = re.compile('class="omvideos">(.*?)<!--einde #omcontent-->', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        youtube = re.compile(r'href="http://www\.youtube\.com(.*?)"', re.IGNORECASE | re.DOTALL).findall(matchyoutube)
        for youtube in youtube:
            youtube = 'http://www.youtube.com' + youtube
            stream = YDStreamExtractor.getVideoInfo(youtube)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)
    except:
        pass
    youtubezoeken = re.compile('div class="attr">Artikelnaam:</div>.*?<div class="spec">(.*?)</div>.*?div class="attr">Merk:</div>.*?<div class="spec">(.*?)</div>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for artikelnaam, importeur in youtubezoeken:
        artikelnaam = utils.striphtml(artikelnaam)
        importeur = utils.striphtml(importeur)
        name = artikelnaam + ' ' + importeur
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(name)
        utils.addDir('Bekijk meer video\'s', url, '', image, '')
    dp.close()
    xbmcplugin.endOfDirectory(utils.addon_handle)
        
    
def Search(url):
    searchUrl = url
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    title = title.replace(' ','+')
    searchUrl = searchUrl + title
    page = page=None
    print "Searching URL: " + searchUrl
    Productlist(searchUrl) 