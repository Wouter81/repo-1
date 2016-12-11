import urllib, urllib2, re, cookielib, os, sys, socket
import xbmc, xbmcplugin, xbmcgui, xbmcaddon

import utils, sqlite3


def Kerstcountdown():
    listhtml = utils.getHtml2('http://www.timeanddate.com/countdown/christmas?p0=16&msg=Kerst&font=cursive')
    icon = 'http://addon.dokitv.nl/kerst/icon.jpg'
    utils.addDir('[B]Kerst (25-12-2016 00:00):[/B]','','',icon)
    utils.addDir('','','',icon)
    try:
        match = re.compile("class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>.*?class=csvg-digit-number>(.*?)</div>.*?label>(.*?)</div>", re.IGNORECASE | re.DOTALL).findall(listhtml)
        for number1, days, number2, hours, number3, minutes, number4, seconds in match:
            name = number1 + ' ' + days + ', ' + number2 + ' ' + hours + ', ' + number3 + ' ' + minutes + ', ' + number4 + ' ' + seconds
            utils.addDir(name,'','',icon)
    except: pass
    xbmcplugin.endOfDirectory(utils.addon_handle)