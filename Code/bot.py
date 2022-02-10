from Code import var

from pyrogram import Client,filters
import logging
import os
from decouple import config
from heroku3 import from_key
from os import getenv


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=var.API_KEY,
           api_hash=var.APP_HASH,
           bot_token=var.TOKEN
)
