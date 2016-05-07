import urllib2
import re
import urlparse

import decryptionUtils as crypt
from .. import common

def compose(url):
    
    common.log("jairoX: " + url)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 
               'Referer': 'http://live9.net/'}
    
    #urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': 'dmw:wiziwig2000@jairox.tk:3128'})))   
    
    req = urllib2.Request(url,None,headers)
    response = urllib2.urlopen(req)
    s = response.read()
    response.close()

    match = re.compile(r'var\s+(\w{4}=[^;]+)').findall(s)
    for var in match:
        exec(var)    
    match = re.compile(r'sw=[\'"]{1,2}([^\'";]+)').findall(s)
    if ("+" in match[0]):
        tmp = match[0].strip('+')
        sw = eval(tmp)
    else:
        sw = match[0]
    match = re.compile(r'ch=[\'"]{1,2}([^\'";]+)').findall(s)
    if ("+" in match[0]):
        tmp = match[0].strip('+')
        ch = eval(tmp)
    else:
        ch = match[0]
    match = re.compile(r'src="([^\'";]+)').findall(s)
    tmpUrl = match[0] + sw + '/' + ch

    req = urllib2.Request(tmpUrl,None,headers)
    response = urllib2.urlopen(req)
    s = response.read()
    response.close()

    unpacked = crypt.doDemystify(s)
    #common.log("jairoX2: " + unpacked)
    #if ('flile' in unpacked):
    match = re.compile(r'(?s)SWFObject\(\'([^\']+).*var\s*flile\s*=\s*\'(.*?)\'.*?tkta\s*=\s*\'(.*?)\'.*?bmakz\s*=\s*\'(.*?)\'.*?st2tas\s*=\s*\'(rtmpe?://)?(.*?)\';').findall(unpacked)
    if (match and match[0].count > 4):  
        swf = match[0][0]		
        flile = match[0][1]
        tkta = match[0][2]
        bmakz = urlparse.unquote(match[0][3])
        prot = match[0][4] != "" and match[0][4] or "rtmp://"
        host = match[0][5]
        rtmp = prot + host
        uri = rtmp + '/flash playpath=' + flile + '?' + tkta + bmakz + ' swfVfy=1 swfUrl=' + swf + ' pageUrl=' + tmpUrl

    else:
        match = re.compile(r'(?s)SWFObject\(\'([^\']+).*?file\',unescape\(\'(.*?)\'.*?streamer\',unescape\(\'(.*?)\'').findall(unpacked)
        if (match and match[0].count > 1):
                swf = match[0][0]
                rtmp = urlparse.unquote(match[0][2])
                flile = urlparse.unquote(match[0][1])
                uri = rtmp + ' playpath=' + flile + ' swfVfy=1 swfUrl=' + swf + ' pageUrl=' + tmpUrl

        else:
            match = re.compile(r"(?s)SWFObject\('([^']+).*flile\s*=\s*'(.*?)'.*?tkta\s*=\s*'(.*?)'.*?st2tas\s*=\s*'(rtmpe?://)?(.*?)';").findall(unpacked)
            if (match and match[0].count > 3):
                swf = match[0][0]
                flile = match[0][1]
                tkta = match[0][2]
                prot = match[0][3] != "" and match[0][3] or "rtmp://"
                rtmp = prot + match[0][4]
                uri = rtmp + ' playpath=' + flile + '?' + tkta + ' swfVfy=1 swfUrl=' + swf + ' pageUrl=' + tmpUrl

            else: uri = "http://no.stream.found"
            
    return uri.replace("rtmpe","rtmp")