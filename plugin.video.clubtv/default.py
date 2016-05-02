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
		("[COLOR red]Algemeen >>[/COLOR] KNVB Official", "user/knvb", "https://www.werkenindesport.nl/files/Nieuws/knvblogo.png"),
		("[COLOR red]Algemeen >>[/COLOR] Ons Oranje", "user/onsoranje", "http://m.onsoranje.nl/images/nieuwe-header-onsoranje.png"),
		("[COLOR red]Algemeen >>[/COLOR] FOX Sport", "user/EredivisieLive", "http://d3.foxsports.nl/images/ml/logos/logo.svg"),
		("[COLOR red]Algemeen >>[/COLOR] Jupiler League", "user/Jupilerleague", "http://maak-agenda.nl/images/jupiler.png"),
		("[COLOR red]Algemeen >>[/COLOR] Voetbal Inside", "user/VITVRTL", "http://www.televizier.nl/Uploads/2015/8/Voetbal-Inside_cropped-100-460-360-90-0.jpg"),
		("[COLOR red]Algemeen >>[/COLOR] UEFA TV", "user/UEFA", "https://yt3.ggpht.com/-McWupq8GGww/AAAAAAAAAAI/AAAAAAAAAAA/T-Il0tDTQ5M/s100-c-k-no/photo.jpg"),
		("[COLOR red]Algemeen >>[/COLOR] FootBall 24h HD", "user/seoseoer86", "http://4.bp.blogspot.com/-R7q6iBTIpeo/VROE3VmVkUI/AAAAAAAAAnM/YGxnYH5mf3A/s1600/soccer24h%2Blogo2.png"),
		("[COLOR red]Algemeen >>[/COLOR] Bundesliga", "user/bundesliga", "https://upload.wikimedia.org/wikipedia/en/thumb/1/15/Bundesliga_logo.svg/1161px-Bundesliga_logo.svg.png"),
		("[COLOR red]Algemeen >>[/COLOR] Serie A", "user/legacalcioserieatim", "http://www.wedstrijdticket.nl/wp-content/uploads/2015/07/serie-A.png"),
		("[COLOR red]Algemeen >>[/COLOR] LaLiga", "user/laliga", "http://usclubsoccer.org/wp-content/uploads/2015/08/LALIGA_LOGO_V_2015-01COLOR-BLANCO-cropped.png"),
		("[COLOR red]Algemeen >>[/COLOR] 442oons", "user/442oons", "http://www.reallusion.com/images/rltv/featuredstory/442oons/Pic01.jpg"),

		("[COLOR green]Eredivisie >>[/COLOR] Ajax TV", "user/ajax", "http://files.webklik.nl/user_files/2014_02/535143/ajax_tv_logo.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] Feyenoord TV", "user/FeyenoordRotterdamTV", "https://thumbs.feyenoord.nl/images/thumbs/c5ebbdc3b7a9c0bb86d0b029cd433896_740_0.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] PSV TV", "user/psveindhoven", "http://www.psv.nl/upload/4fd15c84-fc52-4cb1-bb22-69f24ca6127d_logo-PSV-TV-h97v2.png"),
		("[COLOR green]Eredivisie >>[/COLOR] Heracles TV", "user/HeraclesAlmeloTV", "http://www.heracles.nl/Common/images/heracles-logo.png"),
		("[COLOR green]Eredivisie >>[/COLOR] FC Groningen TV", "user/FCGroningenTV", "http://images.tvuitzendinggemist.nl/images/programs/fc-groningen-tv.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] Vitesse TV",  "user/VitesseTV", "http://www.vitesseinside.nl/wp-content/uploads/2014/11/vitesse-tv-youtube.jpg"),		
		("[COLOR green]Eredivisie >>[/COLOR] NEC TV", "user/NECTVkanaal", "http://www.gelderlander.nl/polopoly_fs/1.1602755.1406642586!/image/image.jpg_gen/derivatives/landscape_800_600/image-1602755.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] PEC Zwolle TV", "user/peczwolletv", "http://www.destentor.nl/polopoly_fs/1.4870291.1433064566!/image/image.jpg_gen/derivatives/portrait_600_800/image-4870291.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] FC Utrecht TV", "user/fcutrecht", "http://oldstars.nl/wp-content/uploads/2015/03/FC-Utrecht.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] AZ TV", "user/AZTV", "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/AZ_Alkmaar.svg/1280px-AZ_Alkmaar.svg.png"),
		("[COLOR green]Eredivisie >>[/COLOR] SC Heerenveen TV", "user/scHeerenveen", "http://voetballogos.nl/mediapool/77/779277/resources/14754275.png"),
		("[COLOR green]Eredivisie >>[/COLOR] Excelsior TV", "user/sbvexcelsior", "http://static.voetbalzone.nl/images/logo/clubs195/1532.gif?v=2"),
		("[COLOR green]Eredivisie >>[/COLOR] ADO Den Haag TV", "user/ADODenHaagTV", "http://adodenhaag.nl/images/logos/teams/ado.png"),
		("[COLOR green]Eredivisie >>[/COLOR] Willem II TV", "user/WillemII", "http://media.voetbaluitslagen.nl/media/teams/1521-willem-ii.png"),
		("[COLOR green]Eredivisie >>[/COLOR] FC Twente TV", "user/FCTwenteTV", "http://www.eredivisie-voetbal.nl/images/twente_phixr.jpg"),
		("[COLOR green]Eredivisie >>[/COLOR] SC Cambuur TV", "user/SCCambuurTV", "http://cambuur.nl/friksbeheer/wp-content/themes/cambuur/images/logo-high.png"),
		("[COLOR green]Eredivisie >>[/COLOR] De Graafschap TV", "user/degraafschapvideo", "http://www.degraafschap.nl/content/img/logo.png"),
		("[COLOR green]Eredivisie >>[/COLOR] Roda JC TV", "user/RodaJCKerkradeTV", "http://voetballogos.nl/mediapool/77/779277/resources/14754456.png"),	

		("[COLOR yellow]Jupiler League >>[/COLOR] Go Ahead Eagles TV", "channel/UCD3rTNWI-2AdprNnsXlC0nQ", "http://www.ga-eagles.nl/wp-content/themes/ga-eagles/images/clubs/GAE.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] Go Ahead Eagles TV 2016", "channel/UCz1dwk_LXm1-CsJ-NXT_cTA", "http://www.ga-eagles.nl/wp-content/themes/ga-eagles/images/clubs/GAE.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] FC Den Bosch TV", "user/FCDBTV", "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/FC_Den_Bosch_logo.svg/200px-FC_Den_Bosch_logo.svg.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] Achilles 29 TV", "user/TVAchilles", "http://www.achilles29.nl/wp-content/uploads/leaguemanager/Achilles29.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] Almere City FC TV", "user/AlmereCityVideo", "https://pbs.twimg.com/profile_images/492047415873003520/Xgoj86JL.jpeg"),
		("[COLOR yellow]Jupiler League >>[/COLOR] FC Dordrecht TV", "user/fcdordrechtnl", "https://pbs.twimg.com/profile_images/1834356179/FC-Dordrecht-_Converted__400x400.jpg"),
		("[COLOR yellow]Jupiler League >>[/COLOR] FC Eindhoven TV", "user/FCEindhovenTV", "http://fc-eindhoven.nl/img/logo-fce.png"),		
		("[COLOR yellow]Jupiler League >>[/COLOR] FC Emmen TV", "channel/UCxHyCHCUnzW_3dqzvfYFIHw", "http://static.voetbalzone.nl/images/logo/clubs195/1539.gif?v=2"),
		("[COLOR yellow]Jupiler League >>[/COLOR] FC Oss TV", "channel/UCsvUne3SPeAUYaNGSkkNLEw", "http://www.fcoss.nl/images/logo.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] Fortuna Sittard TV", "user/FortunaSittardTV", "https://upload.wikimedia.org/wikipedia/en/thumb/2/2d/Fortuna_Sittard_logo.svg/839px-Fortuna_Sittard_logo.svg.png"),		
		("[COLOR yellow]Jupiler League >>[/COLOR] Helmond Sport TV", "user/HelmondSportTV", "http://www.tencate.com/nl/emea/Images/helmond-sport-web26-27359.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] NAC TV", "user/NACBredaNL", "http://www.nac.nl/images/logo_nac_breda_big.png"),
		("[COLOR yellow]Jupiler League >>[/COLOR] RKC TV", "user/RKCWAALWIJKTUBE", "http://www.eredivisie-voetbal.nl/images/logo_rkc_waalwijk_0.jpg"),		
		("[COLOR yellow]Jupiler League >>[/COLOR] VVV Venlo TV", "user/TheOfficialVVVVenlo", "http://www.vvv-venlo.nl/layout/vvv-venlo.png"),

		("[COLOR oranje]Overige >>[/COLOR] FC Barcelona TV", "user/fcbarcelona", "http://assets4.fcbarcelona.com/images/og-logo.cb6aeb6cb.png"),
		("[COLOR oranje]Overige >>[/COLOR] Real Madrid TV", "realmadrid", "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Real_Madrid_CF.svg/732px-Real_Madrid_CF.svg.png"),
		("[COLOR oranje]Overige >>[/COLOR] Bayern Muchen TV", "user/fcbayern", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Logo_FC_Bayern_M%C3%BCnchen.svg/266px-Logo_FC_Bayern_M%C3%BCnchen.svg.png"),
		("[COLOR oranje]Overige >>[/COLOR] Borussia Dortmund TV", "user/bvb", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/2000px-Borussia_Dortmund_logo.svg.png"),
		("[COLOR oranje]Overige >>[/COLOR] Manchester United TV", "channel/UCYF2FotHeGO6cNcldrTHN1g", "https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Manchester_United_FC_crest.svg/758px-Manchester_United_FC_crest.svg.png"),
		("[COLOR oranje]Overige >>[/COLOR] Paris Saint Germain TV", "user/PSGofficiel", "https://upload.wikimedia.org/wikipedia/en/c/ca/New_PSG.png"),
		("[COLOR oranje]Overige >>[/COLOR] Juventus TV", "user/juventus", "http://www.juventus.com/pics/layout/juventus_logo.png"),
		
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
    plugintools.log("kidstime.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()