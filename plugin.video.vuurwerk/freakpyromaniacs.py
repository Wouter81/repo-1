import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import YDStreamExtractor 


#100: freakpyromaniacs.Main()
#101: freakpyromaniacs.List(url)
#102: freakpyromaniacs.Listproducten(url)
#103: freakpyromaniacs.Search(url)  
#104: freakpyromaniacs.Productpage(url)


def Main():
    utils.addDir('Zoeken','http://freakpyromaniacs.com/products/includes/suggest.php?term=',103,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')    
    utils.addDir('','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)    
    utils.addDir('FPM Aanraders','http://freakpyromaniacs.com/products/aanraders/',102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    utils.addDir('CAT 1 Vuurwerk','http://freakpyromaniacs.com/products/cat1/',102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    utils.addDir('50gr/shot','http://freakpyromaniacs.com/products/50gram/',102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')    
    utils.addDir('25gr/shot','http://freakpyromaniacs.com/products/25gram/',102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    
    utils.addDir('','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)    
    utils.addDir('[B]Importeurs (NL)[/B]','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)
    listhtml = utils.getHtml2('http://freakpyromaniacs.com/products/')
    nlimporteurs = re.compile(r'<h3>Importeurs \(NL\)</h3><div class="nice_heading_helper_right"></div></div>(.*?)<div id="categories-4" class="widget_categories widget-area"><div class="nice_heading">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    nlmatch = re.compile('href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(nlimporteurs)
    for importeurpage, name in nlmatch:
        importeurpage = 'http://freakpyromaniacs.com' + importeurpage
        utils.addDir(name,importeurpage,101,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    
    utils.addDir('','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)    
    utils.addDir('[B]Importeurs (BE)[/B]','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)
    beimporteurs = re.compile(r'<h3>Importeurs \(BE\)</h3><div class="nice_heading_helper_right"></div></div>(.*?)<div id="categories-4" class="widget_categories widget-area"><div class="nice_heading">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    bematch = re.compile('href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(beimporteurs)
    for importeurpage, name in bematch:
        importeurpage = 'http://freakpyromaniacs.com' + importeurpage
        utils.addDir(name,importeurpage,101,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    
    utils.addDir('','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)    
    utils.addDir('[B]Importeurs (DE)[/B]','',100,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', Folder=False)
    deimporteurs = re.compile(r'<h3>Importeurs \(DE\)</h3><div class="nice_heading_helper_right"></div></div>(.*?)<br />', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    dematch = re.compile('href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(deimporteurs)
    for importeurpage, name in dematch:
        importeurpage = 'http://freakpyromaniacs.com' + importeurpage
        utils.addDir(name,importeurpage,101,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    utils.addDir('Alle Producten',url,102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', 0)
    try:
        collecties = re.compile('<h3>Collecties</h3><div class="nice_heading_helper_right"></div></div>(.*?)<br />', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        collectiematch = re.compile('href="(.*?)".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(collecties)
        for listpage, name in collectiematch:
            listpage = 'http://freakpyromaniacs.com' + listpage
            utils.addDir(name,listpage,102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', 0)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)


def Listproducten(url, page=None):
    if page:
        form_values = {}
        form_values['pagina'] = str(page)
        listhtml = utils.postHtml(url, form_data=form_values)
    else:
        listhtml = utils.getHtml(url, '')
    match = re.compile('<h2>(.*?)</h2>.*?href="(.*?)"><img src="(.*?)".*?Artnr. (.*?)</div>.*?Vraagprijs (.*?)</b>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name, productpage, img, artikelnummer, prijs in match:
        name = artikelnummer + ': ' + name + ' (' + prijs + ')'
        name = name.decode('latin1').encode('utf8')
        productpage = 'http://freakpyromaniacs.com' + productpage
        img = img.replace('klein','groot')
        utils.addDir(name,productpage,104,img)
    try:
        npage = re.compile(r'value="(\d+)"><input type="submit" value="Volgende', re.DOTALL | re.IGNORECASE).findall(listhtml)[0]
        utils.addDir('Volgende Pagina',url,102,'https://pbs.twimg.com/profile_images/1602372109/FPM_film_logo_begin.jpg', npage)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)    

   
def Productpage(url):
    dp = xbmcgui.DialogProgress()
    dp.create("Vuurwerk TV","Laden van de productinformatie en video's.")
    listhtml = utils.getHtml2(url)
    image = re.compile('<img itemprop="image" src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    match = re.compile('<td height="15" width="130".*?<b>(.*?)</b>.*?<td height="15" width="430".*?>(.*?)</td>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name1, name2 in match:
        name1 = utils.striphtml(name1)
        name1 = name1.replace('\n','').replace('\t','')
        name2 = utils.striphtml(name2)
        name2 = name2.replace('\n','').replace('\t','')
        name = '[B]' + name1 + '[/B]: ' + name2
        if 'Te koop bij o.a' in name: pass
        elif 'Forum' in name: pass
        elif 'Fotos' in name: pass
        else: utils.addDownLink(name, '', 104, image, '')
    utils.addDir('','',104,image, Folder=False)    
    videototaal = re.compile('<td width="100%" align="left" colspan="2">(.*?)</td>', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    try:
        vimeo = re.compile('http://player.vimeo.com/video/(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        vimeo = 'http://player.vimeo.com/video/' + vimeo
        stream = YDStreamExtractor.getVideoInfo(vimeo)
        if stream:
            url = stream.streamURL()
            title = stream.selectedStream()['title']
            title = title.encode('utf-8')
            icon = stream.selectedStream()['thumbnail']
            utils.addDir(title,url,300,icon)
    except:
        pass
    #try:
    youtube = re.compile(r"http://www.youtube.com/embed/(.*?)\?autoplay", re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    youtube = 'http://www.youtube.com/embed/' + youtube + '\?autoplay'
    stream = YDStreamExtractor.getVideoInfo(youtube)
    if stream:
        url = stream.streamURL()
        title = stream.selectedStream()['title']
        title = title.encode('utf-8')
        icon = stream.selectedStream()['thumbnail']
        utils.addDir(title,url,300,icon)
    #except: pass
    youtubezoeken = re.compile('Importeur</b>.*?brand">(.*?)</span>.*?Artikelnaam</b>.*?" >(.*?)</td>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for importeur, artikelnaam in youtubezoeken:
        name = artikelnaam + ' ' + importeur
        url = 'plugin://plugin.video.youtube/search/?q=' + urllib.quote_plus(name)
        utils.addDir('Bekijk meer video\'s', url, '', image, '')
    dp.close()
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def SearchList(keyword):
    form_values = {}
    form_values['t_zoeken'] = keyword
    listhtml = utils.postHtml('http://freakpyromaniacs.com/products/zoeken/', form_data=form_values)
    match = re.compile('<h2>(.*?)</h2>.*?href="(.*?)"><img src="(.*?)".*?Artnr. (.*?)</div>.*?Vraagprijs (.*?)</b>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for name, productpage, img, artikelnummer, prijs in match:
        name = artikelnummer + ': ' + name + ' (' + prijs + ')'
        productpage = 'http://freakpyromaniacs.com' + productpage
        img = img.replace('klein','groot')
        utils.addDir(name,productpage,104,img)
    xbmcplugin.endOfDirectory(utils.addon_handle)    

def Search(url):
    vq = utils._get_keyboard(heading="Zoeken naar...")
    if (not vq): return False, 0
    title = urllib.quote_plus(vq)
    SearchList(title)