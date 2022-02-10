

from pyrogram import Client,filters
import logging
import os
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_KEY = config("API_KEY", default=6, cast=int, "3898418")
    API_HASH = config("API_HASH", "5a82313211da04d63297bd4de436228c")
    TOKEN = config("TOKEN", "5200251156:AAH1Xq-2E3IggbFVY7XtWE-Cvioj5mwS43o")
    OWNER_ID = list(map(int, getenv("OWNER_ID", "5125042013").split()))
    

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
