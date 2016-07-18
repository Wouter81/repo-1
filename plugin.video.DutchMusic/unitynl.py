#-*- coding: utf-8 -*-

import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils


def Main():
    utils.addDir('Unity NL','http://www.unity.nu/Ajax/Unity.Gemist.AjaxArticles.ashx?programName=unity%20nl&RecordsPerPage=9999&_=1468322506603',273,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png','')   
    utils.addDir('Unity NL Cafe','http://www.unity.nu/Ajax/Unity.Gemist.AjaxArticles.ashx?programName=unity%20nl%20cafe&RecordsPerPage=9999&_=1468322506600',273,'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/images/unity-nl.png','')    
    xbmcplugin.endOfDirectory(utils.addon_handle)


def List(url):
    listhtml = utils.getHtml2(url)
    match = re.compile('href="(.*?)">.*?url.....(.*?)..".*?</i>.(.*?)</h2>', re.IGNORECASE | re.DOTALL).findall(listhtml)
    for videopage, img, name in match:
        if '%c3' in videopage: continue
        img = "http://www.unity.nu" + img
        videopage = "http://www.unity.nu" + videopage
        utils.addDownLink(name, videopage, 274, img, '')
    xbmcplugin.endOfDirectory(utils.addon_handle)

def Playvid(url, name):
    listhtml = utils.getHtml(url,'')
    iframe = re.compile('height.*?src="(.*?)"', re.IGNORECASE | re.DOTALL).findall(listhtml)[0]
    dp = xbmcgui.DialogProgress()
    dp.create("DutchMusic","Een ogenblik geduld.")       
    if 'https://player.demediahub.nl/' in iframe:
        iframecontent = utils.getHtml(iframe,'')
        match = re.compile('720p.*?file:."(.*?)".*?label: "1080p"', re.IGNORECASE | re.DOTALL).findall(iframecontent)[-1]
        if match:
            videourl = match
            videourl = videourl.replace("&amp;","&")
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
    else:
        if iframe:
            videourl = iframe
            videourl = 'plugin://plugin.video.youtube/play/?video_id=' + videourl.replace('http://www.youtube.com/embed/','')
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