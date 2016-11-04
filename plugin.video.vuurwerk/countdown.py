import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Afsteekcountdown():
    listhtml = utils.getHtml2('http://www.timeanddate.com/countdown/christmas?iso=20161231T18&p0=1295&msg=Vuurwerk+Afsteken&font=cursive')
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('[B]Vuurwerk Afsteken (31-12-2016 18:00):[/B]','','',icon)
    utils.addDir('','','',icon)
    try:
        match = re.compile("class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>", re.IGNORECASE | re.DOTALL).findall(listhtml)
        for number1, days, number2, hours, number3, minutes, number4, seconds in match:
            name = number1 + ' ' + days + ', ' + number2 + ' ' + hours + ', ' + number3 + ' ' + minutes + ', ' + number4 + ' ' + seconds
            utils.addDir(name,'','',icon)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def Countdownverkoopdagen():
    listhtml = utils.getHtml2('http://www.timeanddate.com/countdown/christmas?iso=20161229T00&p0=1295&msg=Vuurwerk+Verkoopdagen&font=cursive')
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('[B]Vuurwerk Verkoopdagen (29-12-2016 00:00):[/B]','','',icon)
    utils.addDir('','','',icon)
    try:
        match = re.compile("class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>", re.IGNORECASE | re.DOTALL).findall(listhtml)
        for number1, days, number2, hours, number3, minutes, number4, seconds in match:
            name = number1 + ' ' + days + ', ' + number2 + ' ' + hours + ', ' + number3 + ' ' + minutes + ', ' + number4 + ' ' + seconds
            utils.addDir(name,'','',icon)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)
    
def CountdownNieuwjaar():
    listhtml = utils.getHtml2('http://www.timeanddate.com/countdown/newyear?p0=1295&font=cursive')
    icon = 'https://raw.githubusercontent.com/DutchMusic/DutchMusic/master/plugin.video.vuurwerk/icon.png'
    utils.addDir('[B]Nieuwjaar (01-01-2017 00:00):[/B]','','',icon)
    utils.addDir('','','',icon)
    try:
        match = re.compile("class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>", re.IGNORECASE | re.DOTALL).findall(listhtml)
        for number1, days, number2, hours, number3, minutes, number4, seconds in match:
            name = number1 + ' ' + days + ', ' + number2 + ' ' + hours + ', ' + number3 + ' ' + minutes + ', ' + number4 + ' ' + seconds
            utils.addDir(name,'','',icon)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)