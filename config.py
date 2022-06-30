import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME")
Startmesaj = os.environ.get("Startmesaj")
Komutlar = os.environ.get("Komutlar")
GrupStart = os.environ.get("GrupStart")
Support = os.environ.get("Support")
Grup = os.environ.get("Grup")
Sahip = os.environ.get("Sahip")
ozel_list = int(os.environ.get("ozel_list"))
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

# mutsuz_panda 
# mutsuz_panda 
# mutsuz_panda 
