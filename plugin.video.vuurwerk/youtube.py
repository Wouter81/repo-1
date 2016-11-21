import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3
import YDStreamExtractor 

def MainYouTube():
    utils.addDir('Kanalen van merken/importeurs(productvideo\'s)','',122,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    utils.addDir('Kanalen van bekende sites (productvideo\'s)','',123,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    utils.addDir('Overige kanalen','',124,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    utils.addDir('Pyros - Discovery Channel','plugin://plugin.video.youtube/channel/UCWcGhvoQXh_55y9764oJkDw/playlist/PLnHtopLEZhd3D36sFrMmFSGaCJCMtX4xu/','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png')
    utils.addDir('','',124,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png', Folder=False) 
    utils.addDir('[COLOR red]Mis je een kanaal? Geef het door via Facebook: [/COLOR]','','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png', Folder=False) 
    utils.addDir('[COLOR red]http://bit.ly/doki-holland[/COLOR]','','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png', Folder=False) 
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Importeurs():
    utils.addDir('Bonfireworks','plugin://plugin.video.youtube/channel/UC9n5wuf8h4JT-fh7uGp-vuw/','','https://i.ytimg.com/i/9n5wuf8h4JT-fh7uGp-vuw/mq1.jpg?v=509c1ef8')
    utils.addDir('Broekhoff Vuurwerk','plugin://plugin.video.youtube/channel/UCS3Og08319P6CVEwh8gFhRA/','','https://yt3.ggpht.com/-Be1qEnJhCJc/AAAAAAAAAAI/AAAAAAAAAAA/VWp3MF1vVMQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Cafferata Vuurwerk','plugin://plugin.video.youtube/channel/UCpMf5c5tg3egq-nP3Afsmvg/','','https://yt3.ggpht.com/-O1D8FMK3gZo/AAAAAAAAAAI/AAAAAAAAAAA/LSb3QhDBPCQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('China Red','plugin://plugin.video.youtube/channel/UCai84ud869q18sBDhDnPIIA/','','https://yt3.ggpht.com/-o9yM28wH7rs/AAAAAAAAAAI/AAAAAAAAAAA/A4qfhxaezR0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Evolution Fireworks','plugin://plugin.video.youtube/user/EvoFireworks/','','https://yt3.ggpht.com/-DffKFGmb_Ok/AAAAAAAAAAI/AAAAAAAAAAA/xmDhV6dPf-I/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('GBV/Weco Vuurwerk','plugin://plugin.video.youtube/user/bestelvuurwerk/','','https://yt3.ggpht.com/-szIPGQWeObQ/AAAAAAAAAAI/AAAAAAAAAAA/eK9acIk3tVw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Hardix Vuurwerk','plugin://plugin.video.youtube/user/hardixvuurwerk/','','https://yt3.ggpht.com/--fm_Kp-3ahI/AAAAAAAAAAI/AAAAAAAAAAA/IIlO4AvKsHA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Katan Vuurwerk','plugin://plugin.video.youtube/user/katanvuurwerk/','','https://yt3.ggpht.com/-btKB4QxOYpU/AAAAAAAAAAI/AAAAAAAAAAA/fWSdfbG2q80/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Lesli Vuurwerk','plugin://plugin.video.vimeo/user/8315812/videos/','','https://i.vimeocdn.com/portrait/6976022_300x300')
    utils.addDir('Meester Vuurwerk','plugin://plugin.video.youtube/user/MeesterVuurwerk/','','https://yt3.ggpht.com/-0V3SwuKfDt0/AAAAAAAAAAI/AAAAAAAAAAA/fwpA1laZI5s/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Mercurius Vuurwerk','plugin://plugin.video.youtube/user/MercuriusVuurwerk/','','https://yt3.ggpht.com/-nRZtHMNjnMw/AAAAAAAAAAI/AAAAAAAAAAA/5Zo7UWUR-_M/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pronk Vuurwerk','plugin://plugin.video.youtube/user/PyroLitzer/','','https://yt3.ggpht.com/-POE1Iv6Lhq8/AAAAAAAAAAI/AAAAAAAAAAA/pBC_TL2pp6g/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Royal Fireworks','plugin://plugin.video.youtube/channel/UCiCHsb4Kq70tjcxZo81E5dw/','','https://yt3.ggpht.com/-OEz3_EYP81Y/AAAAAAAAAAI/AAAAAAAAAAA/QEscWyXGrAQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Rubro Vuurwerk','plugin://plugin.video.youtube/user/RubroVuurwerkNL/','','https://yt3.ggpht.com/-1bHbXUkqC_k/AAAAAAAAAAI/AAAAAAAAAAA/n0EhKktV4iY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('VDN Fireworks','plugin://plugin.video.youtube/user/vdnfireworks','','https://www.youtube.com/user/vdnfireworks')
    utils.addDir('Vulcan Europe','plugin://plugin.video.youtube/user/vulcaneurope/','','https://yt3.ggpht.com/-6rpJBszVLJ0/AAAAAAAAAAI/AAAAAAAAAAA/tugBXwaPamo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Vuurwerkmania','plugin://plugin.video.youtube/user/vuurwerkmaniatube/','','https://yt3.ggpht.com/-mPEbf5zzuj4/AAAAAAAAAAI/AAAAAAAAAAA/yp2TTMhV9z0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Vuurwerktotaal','plugin://plugin.video.youtube/user/Vuurwerktotaal/','','https://yt3.ggpht.com/-o1nN_y5qQkY/AAAAAAAAAAI/AAAAAAAAAAA/QOPREc9dERU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Wolff Vuurwerk','plugin://plugin.video.youtube/channel/UChYIvqOfgmvRtsz9p0Ioj5Q/','','https://yt3.ggpht.com/-3FdW9OF9gqU/AAAAAAAAAAI/AAAAAAAAAAA/u_ACViv-geE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Zena Vuurwerk','plugin://plugin.video.youtube/user/ZenaVuurwerkNL/','','https://yt3.ggpht.com/-jws2zIxSToI/AAAAAAAAAAI/AAAAAAAAAAA/w5vWucvWNSM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Sites():
    utils.addDir('Vuurwerkbieb','plugin://plugin.video.youtube/user/vuurwerkbieb/','','https://yt3.ggpht.com/-tdnz2pV2-RY/AAAAAAAAAAI/AAAAAAAAAAA/wg6JxcmDIp4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Vuurwerkcrew','plugin://plugin.video.youtube/user/VuurwerkcrewNL/','','https://yt3.ggpht.com/-jOr4SbMQzhw/AAAAAAAAAAI/AAAAAAAAAAA/uHHWUn2XfFA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Freakpyromaniacs','plugin://plugin.video.youtube/user/Freakpyromaniacs/','','https://yt3.ggpht.com/-MtNXCDPcorw/AAAAAAAAAAI/AAAAAAAAAAA/i-7YOirLQJM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Vuurwerkfans','plugin://plugin.video.youtube/channel/UCVkF3yVN6EUAjhToaUJqW4w/','','https://yt3.ggpht.com/-ZGP9KbkQqqU/AAAAAAAAAAI/AAAAAAAAAAA/TDrJycPWU2U/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Overige():
    utils.addDir('Xtremerides1','plugin://plugin.video.youtube/user/Xtremerides1/','','https://yt3.ggpht.com/-99Nn-wf3fiU/AAAAAAAAAAI/AAAAAAAAAAA/RcmMyF2StTk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Limburgs Vuurwerk Team - Professionals in Firework Videos!','plugin://plugin.video.youtube/user/limburgsvuurwerkteam/','','https://yt3.ggpht.com/-oYsgoDEQ-NI/AAAAAAAAAAI/AAAAAAAAAAA/FqvPIjGA6Lg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Firework4000','plugin://plugin.video.youtube/user/firework4000/','','https://yt3.ggpht.com/-ctHjEdGCsZE/AAAAAAAAAAI/AAAAAAAAAAA/l6nAXErUlPU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('baassie123','plugin://plugin.video.youtube/user/baassie123/','','https://yt3.ggpht.com/-OnIVI7sNUZ4/AAAAAAAAAAI/AAAAAAAAAAA/u3jv5R5vjfE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Stefan Works','plugin://plugin.video.youtube/user/Kaboom1555/','','https://yt3.ggpht.com/-xVrmpwbagEw/AAAAAAAAAAI/AAAAAAAAAAA/m0ORJSTTif4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('displayfireworks1','plugin://plugin.video.youtube/user/displayfireworks1/','','https://yt3.ggpht.com/-cTyA9w7409Y/AAAAAAAAAAI/AAAAAAAAAAA/DFFrS91m6hc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Fireworks Show','plugin://plugin.video.youtube/channel/UC_rD92ybuUCNIpUa14ithlg/','','https://yt3.ggpht.com/-VjrOaEtK0sQ/AAAAAAAAAAI/AAAAAAAAAAA/_OeWg8XibfY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('PolskieFajerwerki','plugin://plugin.video.youtube/user/PolskieFajerwerki/','','https://yt3.ggpht.com/-uWv_mHJSR-M/AAAAAAAAAAI/AAAAAAAAAAA/V12te0CNvQM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pyroworld.nl - HD Fireworks Videos','plugin://plugin.video.youtube/user/pyroworldwebsite/','','https://yt3.ggpht.com/-7c6wVK_24RQ/AAAAAAAAAAI/AAAAAAAAAAA/D6fkYsN75Hg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Vuurwerkpunt - Fireworks movies','plugin://plugin.video.youtube/user/Vuurwerkpunt/','','https://yt3.ggpht.com/-JR0ePWP1ndw/AAAAAAAAAAI/AAAAAAAAAAA/sTQKwfpipg0/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('TheGizmo75','plugin://plugin.video.youtube/user/TheGizmo75/','','https://yt3.ggpht.com/-xvzZwIeyrlU/AAAAAAAAAAI/AAAAAAAAAAA/cliGZURQffo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('firework Pollius','plugin://plugin.video.youtube/channel/UC7WZB_Ixbsr9NuPNmPyNmzA/','','https://yt3.ggpht.com/-bxVG26YE8dc/AAAAAAAAAAI/AAAAAAAAAAA/pU7rJ4gMCfc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pyrofreak Grunn','plugin://plugin.video.youtube/channel/UCCjHVXo9tdhztiy8pHO5vwA/','','https://yt3.ggpht.com/-E6HAOGlPG1E/AAAAAAAAAAI/AAAAAAAAAAA/loXRsGEg9Dg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Eindje-Pyro','plugin://plugin.video.youtube/channel/UC87Ra0dmyahLt8AZoj3Nr_Q/','','https://yt3.ggpht.com/-gq5CEBueu3w/AAAAAAAAAAI/AAAAAAAAAAA/7jmb0jBkVo4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Originallover','plugin://plugin.video.youtube/user/Originallover/','','https://yt3.ggpht.com/-jtfdpwt0-8U/AAAAAAAAAAI/AAAAAAAAAAA/I830nLhz6rY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pyrodise','plugin://plugin.video.youtube/channel/UCTw5Ny9VmRQnDb4obDS0Idg/','','https://yt3.ggpht.com/-9zjgLVV86WM/AAAAAAAAAAI/AAAAAAAAAAA/hr1fR7i9nMU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('wwwPIROWEBit','plugin://plugin.video.youtube/user/wwwPIROWEBit/','','https://yt3.ggpht.com/-FDAXDNCYKOo/AAAAAAAAAAI/AAAAAAAAAAA/ukUIM9YiZXg/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pirofan pirotecnia','plugin://plugin.video.youtube/user/PirofanWeb1/','','https://yt3.ggpht.com/-maK3kuoy1jk/AAAAAAAAAAI/AAAAAAAAAAA/jLDvvfbkYJk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('PIROART','plugin://plugin.video.youtube/user/pyroinfo/','','https://yt3.ggpht.com/-i4wkfeNwEc4/AAAAAAAAAAI/AAAAAAAAAAA/6BVAk758FiU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('apirotecnia','plugin://plugin.video.youtube/user/apirotecnia/','','https://i.ytimg.com/i/JfuL60Mtus7YhudU7c6k8Q/mq1.jpg?v=53143662')
    utils.addDir('1PYRO8 - Fireworks from around the world!','plugin://plugin.video.youtube/user/1PYRO8/','','https://yt3.ggpht.com/-HNvXykL__-c/AAAAAAAAAAI/AAAAAAAAAAA/iw_21swRtW8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Startecnia Fireworks','plugin://plugin.video.youtube/user/Startecnia/','','https://yt3.ggpht.com/-a_mfICoZD9M/AAAAAAAAAAI/AAAAAAAAAAA/QzzEdS4WYbA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('vivirlapirotecnia','plugin://plugin.video.youtube/user/vivirlapirotecnia/','','https://yt3.ggpht.com/-LSArzo3UQb4/AAAAAAAAAAI/AAAAAAAAAAA/8irqpMW3P5w/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Pyromovies HD','plugin://plugin.video.youtube/channel/UCh9gTv9eE80rVx3G02jDkjQ/','','https://yt3.ggpht.com/-vfcCnKe8Its/AAAAAAAAAAI/AAAAAAAAAAA/qwe8CQXhjIM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('vuurvent','plugin://plugin.video.youtube/user/vuurvent/','','https://yt3.ggpht.com/-fV-edoXn-kM/AAAAAAAAAAI/AAAAAAAAAAA/q9OCx7-oSGY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    utils.addDir('Re Verser','plugin://plugin.video.youtube/user/ReVerSeR2014/','','https://yt3.ggpht.com/-2zvfTTt96ww/AAAAAAAAAAI/AAAAAAAAAAA/xlMhzsoDf10/s100-c-k-no-mo-rj-c0xffffff/photo.jpg')
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Vuurwerkcrew(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile('<a class="title" href="(.*?)" id=".*?">(.*?)</a>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for page, name in match:
        name = utils.cleantext(name)
        page = 'http://forum.vuurwerkcrew.nl/' + page
        if 'Hulde aan alle leden voor het uploaden !!' in name:
            pass
        elif 'Belangrijk: Hoe plaats ik een youtube filmpje!?' in name:
            pass
        elif 'Met welk programma zet jij je films in elkaar?' in name:
            pass
        else:
            utils.addDir(name,page,127,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    try:
        nextptotaal = re.compile('<li class="navbit lastnavbit"><span>.*?</span></li>(.*?)hreadlist_controls toolsmen', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
        nextp = re.compile('span class="prev_next"><a rel="next" href="(.*?)" title="(.*?)">', re.IGNORECASE | re.DOTALL).findall(nextptotaal)
        for nextpage, nexttitle in nextp:
            nextpage = 'http://forum.vuurwerkcrew.nl/' + nextpage
            utils.addDir(nexttitle,nextpage,126,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    except:
        pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def vuurwerkcrewvideopage(url):
    listhtml = utils.getHtml(url, url)
    match = re.compile('iframe.*?src=".*?youtube.com(.*?)".*?</iframe>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    dp = xbmcgui.DialogProgress()
    count = 0
    dp.create("Vuurwerk TV","Een ogenblik geduld.")      
    if match:
        for videopage in match:
            videopage = 'http://www.youtube.com' + videopage
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)
    else:
        pass
        #utils.addDir('Op deze pagina is geen video gevonden.','','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png', Folder=False)
        #utils.addDir('Probeer de volgende pagina of een andere link.','','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png', Folder=False)

    match = re.compile('<embed width=".*?vimeo.com.*?id=(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)
    if match:
        for videopage in match:
            videopage = 'https://vimeo.com/' + videopage
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)
    else:
        pass
    
    match = re.compile('<a href="(.*?)" title="View this video at YouTube in a new window or tab" target="_blank">YouTube Video</a>', re.IGNORECASE).findall(listhtml)
    if match:
        for videopage in match:
            stream = YDStreamExtractor.getVideoInfo(videopage)
            if stream:
                url = stream.streamURL()
                title = stream.selectedStream()['title']
                title = title.encode('utf-8')
                icon = stream.selectedStream()['thumbnail']
                utils.addDir(title,url,300,icon)
    else:
        pass 
    

    nextptotaal = re.compile('<div id="pagination_top" class="pagination_top"(.*?)<ul class="popupbody popuphover">', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    try:
        nextp = re.compile('span class="prev_next"><a rel="next" href="(.*?)" title="(.*?)">', re.IGNORECASE | re.DOTALL).findall(nextptotaal)
        for nextpage, nexttitle in nextp:
            nextpage = 'http://forum.vuurwerkcrew.nl/' + nextpage
            utils.addDir(nexttitle,nextpage,127,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    except:
        pass

    try:
        lastp = re.compile('<span class="first_last"><a href="(.*?)" title="(.*?)">', re.IGNORECASE).findall(nextptotaal)
        for nextpage, nexttitle in lastp:
            nextpage = 'http://forum.vuurwerkcrew.nl/' + nextpage
            utils.addDir(nexttitle,nextpage,127,'http://www.vuurwerkcrew.nl/skins/vwc/images/logo.jpg')
    except:
        pass
    count = count + 5
    dp.update(count)
    dp.close()
    xbmcplugin.endOfDirectory(utils.addon_handle)