# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Club TV
# (c) 2015 - DOKI
# Based on code from youtube addon
#------------------------------------------------------------
import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.clubtv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
FANART = local.getAddonInfo('fanart')

channellist=[
		("[COLOR darkorange]Algemeen >>[/COLOR] KNVB Official", "user/knvb", "http://dokitv.nl/logo/38.png"),
		("[COLOR darkorange]Algemeen >>[/COLOR] FOX Sport", "user/EredivisieLive", "http://dokitv.nl/logo/36.jpg"),
		("[COLOR darkorange]Algemeen >>[/COLOR] Jupiler League", "user/Jupilerleague", "http://dokitv.nl/logo/37.jpg"),
		("[COLOR darkorange]Algemeen >>[/COLOR] Voetbal Inside", "user/VITVRTL", "http://dokitv.nl/logo/39.jpg"),

		("[COLOR limegreen]Eredivisie >>[/COLOR] ADO Den Haag TV", "user/ADODenHaagTV", "http://dokitv.nl/logo/1.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Ajax TV", "user/ajax", "http://dokitv.nl/logo/2.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] AZ TV", "user/AZTV", "http://dokitv.nl/logo/3.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Excelsior TV", "user/sbvexcelsior", "http://dokitv.nl/logo/4.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Feyenoord TV", "user/FeyenoordRotterdamTV", "http://dokitv.nl/logo/5.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Go Ahead Eagles TV", "channel/UCz1dwk_LXm1-CsJ-NXT_cTA", "http://dokitv.nl/logo/6.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] FC Groningen TV", "user/FCGroningenTV", "http://dokitv.nl/logo/7.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] SC Heerenveen TV", "user/scHeerenveen", "http://dokitv.nl/logo/8.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Heracles TV", "user/HeraclesAlmeloTV", "http://dokitv.nl/logo/9.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] NEC TV", "user/NECTVkanaal", "http://dokitv.nl/logo/10.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] PSV TV", "user/psveindhoven", "http://dokitv.nl/logo/11.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Roda JC TV", "user/RodaJCKerkradeTV", "http://dokitv.nl/logo/12.png"),	
		("[COLOR limegreen]Eredivisie >>[/COLOR] Sparta Rotterdam TV", "channel/UCwABRT8M4wG7JB7jhSv9J7Q", "http://dokitv.nl/logo/13.png"),	
		("[COLOR limegreen]Eredivisie >>[/COLOR] FC Twente TV", "user/FCTwenteTV", "http://dokitv.nl/logo/14.png"),	
		("[COLOR limegreen]Eredivisie >>[/COLOR] FC Utrecht TV", "user/fcutrecht", "http://dokitv.nl/logo/15.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] Vitesse TV",  "user/VitesseTV", "http://dokitv.nl/logo/16.png"),		
		("[COLOR limegreen]Eredivisie >>[/COLOR] Willem II TV", "user/WillemII", "http://dokitv.nl/logo/17.png"),
		("[COLOR limegreen]Eredivisie >>[/COLOR] PEC Zwolle TV", "user/peczwolletv", "http://dokitv.nl/logo/18.png"),
		
		("[COLOR red]Jupiler League >>[/COLOR] Achilles 29 TV", "user/TVAchilles", "http://dokitv.nl/logo/19.png"),
		("[COLOR red]Jupiler League >>[/COLOR] Almere City FC TV", "user/AlmereCityVideo", "http://dokitv.nl/logo/20.png"),
		("[COLOR red]Jupiler League >>[/COLOR] SC Cambuur TV", "user/SCCambuurTV", "http://dokitv.nl/logo/21.png"),
		("[COLOR red]Jupiler League >>[/COLOR] De Graafschap TV", "user/degraafschapvideo", "http://dokitv.nl/logo/22.png"),
		("[COLOR red]Jupiler League >>[/COLOR] FC Den Bosch TV", "user/FCDBTV", "http://dokitv.nl/logo/23.png"),
		("[COLOR red]Jupiler League >>[/COLOR] FC Dordrecht TV", "user/fcdordrechtnl", "http://dokitv.nl/logo/24.png"),
		("[COLOR red]Jupiler League >>[/COLOR] FC Eindhoven TV", "user/FCEindhovenTV", "http://dokitv.nl/logo/25.png"),
		("[COLOR red]Jupiler League >>[/COLOR] FC Emmen TV", "channel/UCxHyCHCUnzW_3dqzvfYFIHw", "http://dokitv.nl/logo/26.png"),
		("[COLOR red]Jupiler League >>[/COLOR] Fortuna Sittard TV", "user/FortunaSittardTV", "http://dokitv.nl/logo/27.png"),
		("[COLOR red]Jupiler League >>[/COLOR] Helmond Sport TV", "user/HelmondSportTV", "http://dokitv.nl/logo/28.png"),
		("[COLOR red]Jupiler League >>[/COLOR] MVV Maastricht TV", "channel/UCwAR0K0Odw9oURKI9y3PbKA", "http://dokitv.nl/logo/29.png"),
		("[COLOR red]Jupiler League >>[/COLOR] NAC TV", "user/NACBredaNL", "http://dokitv.nl/logo/30.png"),	
		("[COLOR red]Jupiler League >>[/COLOR] FC Oss TV", "channel/UCsvUne3SPeAUYaNGSkkNLEw", "http://dokitv.nl/logo/31.png"),
		("[COLOR red]Jupiler League >>[/COLOR] RKC TV", "user/RKCWAALWIJKTUBE", "http://dokitv.nl/logo/32.png"),	
		("[COLOR red]Jupiler League >>[/COLOR] FC Volendam TV", "user/webmasterfcvolendam", "http://dokitv.nl/logo/33.png"),
		("[COLOR red]Jupiler League >>[/COLOR] VVV Venlo TV", "user/TheOfficialVVVVenlo", "http://dokitv.nl/logo/34.png"),	
		
]



# Entry point
def run():
    plugintools.log("clubtv.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("clubtv.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()