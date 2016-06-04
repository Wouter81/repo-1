import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.DOKITube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
FANART = local.getAddonInfo('fanart')

channellist=[
		("DOKI Build Tutorials", "channel/UCAIB9JsLfsleqmsbLDpIlzg/playlist/PLe4X0zmsX_hkNl97AjdlMiROqr-4XC_4e", "https://www.mupload.nl/img/hbbhhrqhufz5r.png"),		
		("Addon Tutorials", "channel/UCAIB9JsLfsleqmsbLDpIlzg/playlist/PLe4X0zmsX_hl5EME_j5AIWVd40qNEXrlx", "https://www.mupload.nl/img/hbbhhrqhufz5r.png"),
		("[COLOR lime]Website :[/COLOR] www.DOKITV.nl", "channel/UCAIB9JsLfsleqmsbLDpIlzg/playlists", "https://www.mupload.nl/img/hbbhhrqhufz5r.png"),		
		("[COLOR lime]Facebook :[/COLOR] http://bit.ly/doki-holland", "channel/UCAIB9JsLfsleqmsbLDpIlzg/playlists", "https://www.mupload.nl/img/hbbhhrqhufz5r.png"),	
]



# Entry point
def run():
    plugintools.log("DOKI.Youtube.run")
    
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
    plugintools.log("DOKI.Youtube.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()