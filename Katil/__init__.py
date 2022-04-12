# Powered By: © heartbrokenperson1
# Copyright (C) 2022 @KatilXUpdates

from telethon import TelegramClient
from Katil.Conf import Config
import logging
 
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

bot = TelegramClient('Saurabh', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Saurabh = bot.start(bot_token=Config.TOKEN)
