import urllib2
import re

def compose(url):    
    req = urllib2.Request(url,None,{'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'})
    response = urllib2.urlopen(req)
    s = response.read()
    response.close()
    match = re.compile(r'var\s+(\w{4}=[^;]+)').findall(s)
    for var in match:
        exec(var)    
    match = re.compile(r'sw=(.*?);').findall(s)
    sw = eval(match[0])
    match = re.compile(r'ch=(.*?);').findall(s)
    ch = eval(match[0])
    match = re.compile(r'src="(.*?)\'').findall(s)
    uri = match[0] + sw + '/' + ch
    return uri

