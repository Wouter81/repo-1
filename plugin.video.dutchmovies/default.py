import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.dutchmovies'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Nederlandse films", "playlist/PLwZj5jiLW6kxWVZJAocTrkjZn_z5aU17R", 'https://www.mupload.nl/img/yh3dab22pno80.png'),
		("Films met ingebakken subs", "playlist/PLwZj5jiLW6kzdzaSR3iX_t6M6UaI_QHMO", 'https://www.mupload.nl/img/yh3dab22pno80.png'),
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
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()