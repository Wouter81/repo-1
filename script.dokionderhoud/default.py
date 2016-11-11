import urllib,urllib2,re,uuid,time
import extract
import xbmcgui,xbmcplugin
import os
from addon.common.net import Net
net=Net()

AddonTitle="DOKI Onderhoud"
thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'script.dokionderhoud')
mediaPath = os.path.join(addonPath, 'media')
dokifanart = os.path.join(addonPath, 'fanart.jpg')
databasePath = xbmc.translatePath('special://database')
base='http://xml.dokitv.nl/'
dialog = xbmcgui.Dialog()

import utils

#######################################################################
#                          CLASSES
#######################################################################

class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi
        



        
#######################################################################
#						Define Menus
#######################################################################

def mainMenu():
    xbmc.executebuiltin("Container.SetViewMode(500)")
    addItem('[B][COLOR lime]C[/COLOR]ache Legen[/B]','url', 1,os.path.join(mediaPath, "1.png"))
    addItem('[B][COLOR lime]T[/COLOR]humbnails Verwijderen[/B]', 'url', 2,os.path.join(mediaPath, "2.png"))
    addItem('[B][COLOR lime]P[/COLOR]ackages Verwijderen[/B]', 'url', 3,os.path.join(mediaPath, "3.png"))
    addItem('[B][COLOR lime]V[/COLOR]erwijder addons.db[/B]', 'url', 8,os.path.join(mediaPath, "4.png"))	
    #addItem('[B][COLOR lime]Z[/COLOR]ero Cache[/B]',base+'0cache.xml', 4,os.path.join(mediaPath, "thumbs.png"))
    #addItem('[B][COLOR lime]C[/COLOR]heck Zero Cache[/B]', 'url', 5,os.path.join(mediaPath, "thumbs.png"))
    #addItem('[B][COLOR lime]V[/COLOR]erwijder Zero Cache[/B]', 'url', 6,os.path.join(mediaPath, "thumbs.png"))	
    addItem('[B][COLOR lime]K[/COLOR]odi Versie[/B]', 'url', 7,os.path.join(mediaPath, "5.png"))	
    addItem('[B][COLOR lime]F[/COLOR]abrieksInstellingen[/B]', 'url', 9,os.path.join(mediaPath, "6.png"))	
    #addItem('[B][COLOR lime]C[/COLOR]ontact[/B]','url',13,os.path.join(mediaPath, "thumbs.png"))
    addItem('[B][COLOR lime]D[/COLOR]OKI Installer[/B]', 'url', 10,os.path.join(mediaPath, "7.png"))
    #addItem('[B][COLOR lime]D[/COLOR]OKI Fix[/B]', 'url', 12,os.path.join(mediaPath, "thumbs.png"))	
    addItem('[B][COLOR lime]D[/COLOR]OKI Nieuws Flits[/B]', 'url', 11,os.path.join(mediaPath, "8.png"))					    
#######################################################################
#						Add to menus
#######################################################################

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


def addDir(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
    
def addDir2(name,url,mode,iconimage,fanart,description,genre,date,credits,showcontext=False,Folder=True):
        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        ok=True
        if date == '':
            date = None
        else:
            description += '\n\nDate: %s' %date
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description, "Genre": genre, "dateadded": date, "credits": credits })
        liz.setProperty("Fanart_Image", fanart)
        if showcontext:
            contextMenu = []
            if showcontext == 'source':
                if name in str(SOURCES):
                    contextMenu.append(('Remove from Sources','XBMC.RunPlugin(%s?mode=8&name=%s)' %(sys.argv[0], urllib.quote_plus(name))))
            elif showcontext == 'download':
                contextMenu.append(('Download','XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(url), urllib.quote_plus(name))))
            elif showcontext == 'fav':
                contextMenu.append(('Remove from DutchMusic Favorites','XBMC.RunPlugin(%s?mode=6&name=%s)'
                                    %(sys.argv[0], urllib.quote_plus(name))))
                                    
            if not name in FAV:
                contextMenu.append(('Add to DutchMusic Favorites','XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
                         %(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(url), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), mode)))
            liz.addContextMenuItems(contextMenu)
        liz.setArt({'fanart': dokifanart})
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=Folder)

        return ok
    
def addItem(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage,)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setArt({'fanart': dokifanart})
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

#######################################################################
#						Parses Choice
#######################################################################
      
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
			params=sys.argv[2]
			cleanedparams=params.replace('?','')
			if (params[len(params)-1]=='/'):
					params=params[0:len(params)-2]
			pairsofparams=cleanedparams.split('&')
			param={}
			for i in range(len(pairsofparams)):
					splitparams={}
					splitparams=pairsofparams[i].split('=')
					if (len(splitparams))==2:
							param[splitparams[0]]=splitparams[1]
							
	return param   

#######################################################################
#						Work Functions
#######################################################################
def setupCacheEntries():
    entries = 5 #make sure this refelcts the amount of entries you have
    dialogName = ["MP3 Streams", "4oD", "BBC iPlayer", "Simple Downloader", "ITV"]
    pathName = ["special://profile/addon_data/plugin.audio.mp3streams/temp_dl", "special://profile/addon_data/plugin.video.4od/cache",
					"special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache","special://profile/addon_data/script.module.simple.downloader",
                    "special://profile/addon_data/plugin.video.itv/Images"]
                    
    cacheEntries = []
    
    for x in range(entries):
        cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return cacheEntries


def clearCache():
    
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("DOKI Onderhoud", str(file_count) + " bestanden gevonden", "Weet je zeker dat je ze wil verwijderen?"):
                
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("DOKI Onderhoud", str(file_count) + " bestanden gevonden", "Weet je zeker dat je ze wil verwijderen?"):
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'Other'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("Delete ATV2 Cache Files", str(file_count) + " files found in 'LocalAndRental'", "Do you want to delete them?"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    
                
    cacheEntries = setupCacheEntries()
                                         
    for entry in cacheEntries:
        clear_cache_path = xbmc.translatePath(entry.path)
        if os.path.exists(clear_cache_path)==True:    
            for root, dirs, files in os.walk(clear_cache_path):
                file_count = 0
                file_count += len(files)
                if file_count > 0:

                    dialog = xbmcgui.Dialog()
                    if dialog.yesno("Raw Manager",str(file_count) + "%s cache files found"%(entry.name), "Do you want to delete them?"):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
                

    dialog = xbmcgui.Dialog()
    dialog.ok("Doki Onderhoud", "Je cache is geleegd!")

    
def deleteThumbnails():
    if os.path.exists(thumbnailPath)==True:  
            if dialog.yesno("DOKI Onderhoud", "Deze optie verwijderd alle thumbnails", "Weet u zeker dat u deze wilt verwijderen?"):
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
                                pass
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    try:
        os.unlink(text13)
    except:
        try:
            dbcon = sqlite3.connect(text13)
            dbcur = dbcon.cursor()
            dbcur.execute('DROP TABLE IF EXISTS path')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute('DROP TABLE IF EXISTS sizes')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute('DROP TABLE IF EXISTS texture')
            dbcur.execute('VACUUM')
            dbcon.commit()
            dbcur.execute("""CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))"""
                          )
            dbcon.commit()
            dbcur.execute("""CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)"""
                          )
            dbcon.commit()
            dbcur.execute("""CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))"""
                          )
            dbcon.commit()
        except:
            pass
        
    dialog.ok("DOKI Onderhoud", "Herstart uw systeem om de thumbnail map weer op te bouwen")
	        
def purgePackages():
    
    purgePath = xbmc.translatePath('special://home/addons/packages')
    dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    if dialog.yesno("DOKI Onderhoud", "%d packages gevonden."%file_count, "Wil je ze verwijderen?"):  
        for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                dialog = xbmcgui.Dialog()
                dialog.ok("DOKI Onderhoud", "Alle Packages zijn verwijderd.")
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok("DOKI Onderhoud", "Geen Packages om te verwijderen.")
		
def ADVANCEDXML(url,name):
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    dialog = xbmcgui.Dialog()
    bak=os.path.join(path, 'advancedsettings.xml.bak')
    if os.path.exists(bak)==False: 
        if dialog.yesno("DOKI Onderhoud",'Je gaat nu de zero cache tweak installeren.','',):
            print '###'+AddonTitle+' - ADVANCED XML###'
            path = xbmc.translatePath(os.path.join('special://home/userdata',''))
            advance=os.path.join(path, 'advancedsettings.xml')
            try:
                os.remove(advance)
                print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
            except:
                pass
            link=net.http_GET(url).content
            a = open(advance,"w") 
            a.write(link)
            a.close()
            print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
            dialog = xbmcgui.Dialog()
            dialog.ok(AddonTitle,"Klaar!")
    else: 
        print '###'+AddonTitle+' - ADVANCED XML###'
        path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        advance=os.path.join(path, 'advancedsettings.xml')
        try:
            os.remove(advance)
            print '=== Maintenance Tool - REMOVING    '+str(advance)+'    ==='
        except:
            pass
        link=net.http_GET(url).content
        a = open(advance,"w") 
        a.write(link)
        a.close()
        print '=== Maintenance Tool - WRITING NEW    '+str(advance)+'    ==='
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle,"Klaar!")    
    
def CHECKADVANCEDXML(url,name):
    print '###'+AddonTitle+' - CHECK ADVANCE XML###'
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        a=open(advance).read()
        if 'zero' in a:
            name='[COLOR lime]aan[/COLOR]'
        elif 'tuxen' in a:
            name='TUXENS'
    except:
        name="[COLOR red]uit[/COLOR]"
    dialog = xbmcgui.Dialog()
    dialog.ok(AddonTitle,"Zero cache staat "+ name+" !")
       
def DELETEADVANCEDXML(url):
    print '###'+AddonTitle+' - DELETING ADVANCE XML###'
    path = xbmc.translatePath(os.path.join('special://home/userdata',''))
    advance=os.path.join(path, 'advancedsettings.xml')
    try:
        os.remove(advance)
        dialog = xbmcgui.Dialog()
        print '=== Maintenance Tool - DELETING    '+str(advance)+'    ==='
        dialog.ok(AddonTitle, "Zero cache is verwijderd.")
    except:
        dialog = xbmcgui.Dialog()
        dialog.ok(AddonTitle, "Zero cache is niet ingeschakeld.")
		
def KODIVERSION(url): xbmc_version=xbmc.getInfoLabel("System.BuildVersion"); version=xbmc_version[:4]; print version; dialog=xbmcgui.Dialog(); dialog.ok(AddonTitle, "Jouw Kodi Versie is : [COLOR lime][B]%s[/B][/COLOR]" % version)

def removeAddonsDatabase():
    dbList = os.listdir(databasePath)
    dbAddons = []
    removed = True
    for file in dbList:
        if re.findall('Addons(\d+)\.db', file):
            dbAddons.append(file)
    for file in dbAddons:
        dbFile = os.path.join(databasePath, file)
        try:
            os.unlink(dbFile)
        except:
            removed = False
    if removed:
        dialog.ok("DOKI Onderhoud", "Herstart uw systeem om addons database weer op te bouwen")
    else:
        dialog.ok("DOKI Onderhoud", "Het verwijderen is mislukt!", "U zou dit handmatig moeten doen")
		
def factoryreset(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.video.freshstart')))
    if pluginpath: xbmc.executebuiltin("RunAddon(plugin.video.freshstart)")
    else:
        url=base+'plugin.video.freshstart.zip'; path=xbmc.translatePath(os.path.join('special://home','addons','packages')); lib=os.path.join(path,'plugin.video.freshstart.zip'); DownloaderClass(url,lib)
        time.sleep(3)
        addonfolder=xbmc.translatePath(os.path.join('special://home','addons','')); dp=xbmcgui.DialogProgress(); print '=== INSTALLING Fresh Start ==='; dp.create(AddonTitle,"Extracting Zip Please Wait")
        extract.all(lib,addonfolder,dp); xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); xbmc.executebuiltin("RunAddon(plugin.video.freshstart)")		

def stuurbericht():
    dialog.ok('Stuur een bericht','Vul in de volgende vensters je naam, e-mail adres en het bericht in.')
    naam = utils._get_keyboard(heading='Naam')
    if (not naam): 
        utils.notify('Niet verzonden','Er is geen naam ingevuld.')
        return False
    email = utils._get_keyboard(heading='E-mail adres')
    if (not email):
        utils.notify('Niet verzonden','Er is geen e-mail adres ingevuld.')
        return False
    bericht = utils._get_keyboard(heading='Bericht')
    if (not bericht):
        utils.notify('Niet verzonden','Er is geen bericht ingevuld.')
        return False
    form_values = {}
    form_values['bezoeker_naam'] = naam
    form_values['bezoeker_email'] = email
    form_values['bezoeker_bericht'] = bericht
    result = utils.postHtml('http://dutchmusic.ml/dokionderhoud/versturen.php', form_data=form_values)
    utils.notify('Bericht Verzonden','')


def dokiinstall(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.program.dokiinstaller')))
    if pluginpath: xbmc.executebuiltin("RunAddon(plugin.program.dokiinstaller)")
    else:
        url=base+'plugin.program.dokiinstaller.zip'; path=xbmc.translatePath(os.path.join('special://home','addons','packages')); lib=os.path.join(path,'plugin.program.dokiinstaller.zip'); DownloaderClass(url,lib)
        time.sleep(3)
        addonfolder=xbmc.translatePath(os.path.join('special://home','addons','')); dp=xbmcgui.DialogProgress(); print '=== INSTALLING Fresh Start ==='; dp.create(AddonTitle,"Extracting Zip Please Wait")
        extract.all(lib,addonfolder,dp); xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); xbmc.executebuiltin("RunAddon(plugin.program.dokiinstaller)")	

def dokifix(url):
    pluginpath=os.path.exists(xbmc.translatePath(os.path.join('special://home','addons','plugin.program.dokifix')))
    if pluginpath: xbmc.executebuiltin("RunAddon(plugin.program.dokifix)")
    else:
        url=base+'plugin.program.dokifix.zip'; path=xbmc.translatePath(os.path.join('special://home','addons','packages')); lib=os.path.join(path,'plugin.program.dokifix.zip'); DownloaderClass(url,lib)
        time.sleep(3)
        addonfolder=xbmc.translatePath(os.path.join('special://home','addons','')); dp=xbmcgui.DialogProgress(); print '=== INSTALLING Fresh Start ==='; dp.create(AddonTitle,"Extracting Zip Please Wait")
        extract.all(lib,addonfolder,dp); xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); xbmc.executebuiltin("RunAddon(plugin.program.dokifix)")					

def DownloaderClass(url,dest, useReq = False):
    dp = xbmcgui.DialogProgress()
    dp.create(AddonTitle,"Bestanden downloaden.",'')

    if useReq:
        import urllib2
        req = urllib2.Request(url)
        req.add_header('Referer', 'http://wallpaperswide.com/')
        f       = open(dest, mode='wb')
        resp    = urllib2.urlopen(req)
        content = int(resp.headers['Content-Length'])
        size    = content / 100
        total   = 0
        while True:
            if dp.iscanceled(): 
                raise Exception("Canceled")                
                dp.close()

            chunk = resp.read(size)
            if not chunk:            
                f.close()
                break

            f.write(chunk)
            total += len(chunk)
            percent = min(100 * total / content, 100)
            dp.update(percent)       
    else:
        urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))

def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        raise Exception("Canceled")
        dp.close()				

def Nieuws():
	text = ''
	twit = 'https://raw.githubusercontent.com/doki1/dokitvnl/master/DOKI%20Tools%20XML/DOKINieuws.xml'
	req = urllib2.Request(twit)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	match=re.compile("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)
	for status, dte in match:
	    try:
			    status = status.decode('ascii', 'ignore')
	    except:
			    status = status.decode('utf-8','ignore')
	    dte = dte[:-15]
	    status = status.replace('&amp;','')
	    dte = '[COLOR lime][B]'+dte+'[/B][/COLOR]'
	    text = text+dte+'\n'+status+'\n'+'\n'
	showText('[COLOR lime]Doki Nieuws Flits[/COLOR]', text)	

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
	try:
	    xbmc.sleep(10)
	    retry -= 1
	    win.getControl(1).setLabel(heading)
	    win.getControl(5).setText(text)
	    return
	except:
	    pass
					
		
		
		
#######################################################################
#						START MAIN
#######################################################################              


params=get_params()
url=None
name=None
mode=None
fanart=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:    
		fanart=urllib.unquote_plus(params["fanart"])
except: 
		pass		

if mode==None or url==None or len(url)<1:
        mainMenu()
       
elif mode==1:
		clearCache()
        
elif mode==2:
        deleteThumbnails()

elif mode==3:
		purgePackages()
		
elif mode==4:
		ADVANCEDXML(url,name)
		
elif mode==5:
		CHECKADVANCEDXML(url,name)	

elif mode==6:
		DELETEADVANCEDXML(url)			

elif mode==7:
		KODIVERSION(url)
		
elif mode==8:
    removeAddonsDatabase()		

elif mode==9:
    factoryreset(url)	

elif mode==10:
    dokiinstall(url)
	
elif mode==11:	
	Nieuws()	

elif mode==12:
    dokifix(url)	

elif mode==13:
    stuurbericht()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

