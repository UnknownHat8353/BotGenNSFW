import os
import sys
import json
import time
import requests
import websocket
from websocket import WebSocket
from json import dumps
from server import server_on

status = "idle" #online/dnd/idle

custom_status = "https://cdn.discordapp.com/attachments/1329442639694790746/1329856830687547413/Untitled30_20250117235554.png?ex=678bdd2f&is=678a8baf&hm=f6d35359f2309ee5d1f6f343e8c852b7e43b2dbb38814b4e46e66c1c6eb7b5db&" #If you don't need a custom status on your profile, just put "" instead of "youtube.com/@SealedSaucer"

usertoken = "TOKEN"
server_id = 1248847484692856833 # ไอดีเซิร์ฟ
channel_id = 1304096722213015553 # ไอดีช่องเสียง


if not usertoken:
    print("[ERROR] Please add a token inside Secrets.")
    sys.exit()

headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers)
if validate.status_code != 200:
    print("[ERROR] Your token might be invalid. Please check it again.")
    sys.exit()

userinfo = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def onliner():
    ws_voice = WebSocket()
    ws_voice.connect("wss://gateway.discord.gg/?v=8&encoding=json")
    ws_voice.send(dumps(
        {
            "op": 2,
            "d": {
                "token": usertoken,
                "properties": {
                    "$os": "windows",
                    "$browser": "Discord",
                    "$device": "desktop"
                }
            }
        }))
    ws_voice.send(dumps({
        "op": 4,
        "d": {
            "guild_id": server_id,
            "channel_id": channel_id,
            "self_mute": True,
            "self_deaf": True, 
            "self_stream?": True, 
            "self_video": True
        }
    }))
    ws_voice.send(dumps({
        "op": 18,
        "d": {
            "type": "guild",
            "guild_id": server_id,
            "channel_id": channel_id,
            "preferred_region": "spain"
        }
    }))
    ws_voice.send(dumps({
        "op": 1,
        "d": None
    }))
    
server_on()

onliner(os.getenv('TOKEN'))
