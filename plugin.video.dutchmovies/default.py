import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.dutchmovies'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
FANART = local.getAddonInfo('fanart')

channellist=[
        ("[COLOR darkorange]Nederlandse films[/COLOR]", "playlist/PLwZj5jiLW6kxWVZJAocTrkjZn_z5aU17R", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Films met ingebakken subs[/COLOR]", "playlist/PLwZj5jiLW6kzdzaSR3iX_t6M6UaI_QHMO", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]YT Kanaal: PolitieNostalgie[/COLOR]", "user/PolitieNostalgie", "https://yt3.ggpht.com/-WPXk_n6TycA/AAAAAAAAAAI/AAAAAAAAAAA/p8OxAn9eylY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
		
		("[COLOR darkorange]YT Kanaal: Tv Series[/COLOR]", "channel/UClOL0I_2CsJTBd3Pfd2yrGw", "https://www.mupload.nl/img/nkskln9iwquob.jpg"),
		
		("[COLOR darkorange]Nederlandse serie's: Toen was geluk heel gewoon[/COLOR]", "playlist/PL93_4h9baNvOKPSwNPLc0ye9agfteowfq", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Nederlandse serie's: Unit 13[/COLOR]", "playlist/PLoNJZg83zwjF8CI_VmY2D5BBMg607OF48", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Nederlandse serie: Van Speijk[/COLOR]", "playlist/PLwZj5jiLW6kwN9WignsLB5KP-Z1PPDaVM", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Nederlandse serie: Bureau Kruislaan[/COLOR]", "playlist/PLwZj5jiLW6kxkyGxz3mQiL6nH70-sW1lP", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Nederlandse serie: Grijpstra & De Gier[/COLOR]", "playlist/PLwZj5jiLW6kw5W_8Lv4HSMFbP46i45h9o", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		("[COLOR darkorange]Nederlandse serie: Combat[/COLOR]", "playlist/PL1B6577408F8038C7", "https://www.mupload.nl/img/yh3dab22pno80.png"),
		
		
		
        ]



# Entry point
def run():
    plugintools.log("NLMovies.run")
    
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
    plugintools.log("NLMovies.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()