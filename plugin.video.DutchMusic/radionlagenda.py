import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def List(url):
    utils.addDir('Uitzending Gemist','plugin://plugin.video.youtube/channel/UCjclCX8plTF5kX4i2KbkbtQ/','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png')
    #utils.addDir('','','','https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png')
    utils.addDir('[B][COLOR red]RADIONL Live Uitzendingen:[/COLOR][/B]','',258,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png')
    utils.addDir('Elke Werkdag - RADIONL','',259,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png')
    url = 'http://www.radionl.fm/agenda/'
    listhtml = utils.getHtml(url,'')
    match = re.compile('<h1 style=".*?">(.*?)<br />(.*?)</h1>.*?href="(.*?)".*?<h3>(.*?)</h3>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for date1, date2, img, name in match:
        if 'Zomertoer' or 'MPF' or 'TV Oranje' or 'Mega' or 'Zomertour' or 'RADIONL Live' in name:
            imgext = ['jpg', 'png']
            if any(x in img for x in imgext):
                name = date1 + ' ' + date2 + ' - ' + name
                utils.addDir(name, '', 259, img, '')
            else: 
                name = date1 + ' ' + date2 + ' - ' + name
                img = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png'
                utils.addDir(name, '', 259, img, '')                
        elif 'Drive' in name:
            imgext = ['jpg', 'png']
            if any(x in img for x in imgext):
                name = date1 + ' ' + date2 + ' - ' + name
                utils.addDir(name, '', 260, img, '')
            else:
                name = date1 + ' ' + date2 + ' - ' + name
                img = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png'
                utils.addDir(name, '', 260, img, '')                
        else:
            imgext = ['jpg', 'png']
            if any(x in img for x in imgext):
                name = date1 + ' ' + date2 + ' - ' + name
                utils.addDir(name, '', 261, img, '')
            else:
                name = date1 + ' ' + date2 + ' - ' + name
                img = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/radionl-agenda.png'
                utils.addDir(name, '', 261, img, '')                
    xbmcplugin.endOfDirectory(utils.addon_handle)

def MainTVRADIO():
    utils.addDir('TV 1: ' + xbmc.getInfoLabel("ListItem.Title"), 'http://highvolume04.streampartner.nl/radionl/livestream/playlist.m3u8', 300, xbmc.getInfoImage("ListItem.Thumb"), '')
    utils.addDir('TV 2: ' + xbmc.getInfoLabel("ListItem.Title"), 'rtmp://highvolume04.streampartner.nl:80/radionl/ playpath=livestream swfUrl=http://p.jwpcdn.com/6/12/jwplayer.flash.swf pageUrl=http://media.streampartner.nl/player.php?url=2d784ec170a627160049', 300, xbmc.getInfoImage("ListItem.Thumb"), '')
    utils.addDir('YouTube: ' + xbmc.getInfoLabel("ListItem.Title"), 'plugin://plugin.video.youtube/kodion/search/query/?event_type=live&q=RADIONL&amp;search_type=video', '', xbmc.getInfoImage("ListItem.Thumb"), '')
    utils.addDir('RADIO: ' + xbmc.getInfoLabel("ListItem.Title"), 'http://178.19.127.4:7004/;', 300, xbmc.getInfoImage("ListItem.Thumb"), '') 
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def MainRADIO():
    utils.addDir('RADIO: ' + xbmc.getInfoLabel("ListItem.Title"), 'http://178.19.127.4:7004/;', 300, xbmc.getInfoImage("ListItem.Thumb"), '') 
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def MainGeenStream():
    utils.addDir('Geen Stream Beschikbaar: ' + xbmc.getInfoLabel("ListItem.Title"), '', 258, xbmc.getInfoImage("ListItem.Thumb"), '') 
    xbmcplugin.endOfDirectory(utils.addon_handle)