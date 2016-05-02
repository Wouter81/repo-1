import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.audio.youtube.chrisvalentine'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
FANART = local.getAddonInfo('fanart')

channellist=[
		("[COLOR darkgoldenrod][B]**********Welcome to my Youtube channel**********[/B][/COLOR]","channel/UCoaVnQYgQCoBHcVinZqvjYw","https://www.mupload.nl/img/jr4mdg9awgu.png"),
		("Chris Valentine Official Youtube Channel","channel/UCoaVnQYgQCoBHcVinZqvjYw","https://www.mupload.nl/img/jr4mdg9awgu.png"),
		("Chris Valentine TV","channel/UCIjypyEF8ImpMh4RDa-PGow","https://www.mupload.nl/img/jr4mdg9awgu.png"),
		(" ","channel/UCoaVnQYgQCoBHcVinZqvjYw","https://www.mupload.nl/img/jr4mdg9awgu.png"),
		("[COLOR darkgoldenrod][B]Like us on Facebook bit.ly/chris-valentine[/B][/COLOR]","channel/UCoaVnQYgQCoBHcVinZqvjYw","https://www.mupload.nl/img/jr4mdg9awgu.png"),				
				
]



# Entry point
def run():
    plugintools.log("chrisvalentine.run")
    
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
    plugintools.log("chrisvalentine.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,fanart=FANART,folder=True )



run()