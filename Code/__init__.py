

from pyrogram import Client,filters
import logging
import os
from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_KEY = config("API_KEY", default=6, cast=int, "15257107")
    API_HASH = config("API_HASH", "ce4441ebf27e3591d3d3c1632e783d7a")
    TOKEN = config("TOKEN", "5042510749:AAGQlDtZa4hw2SsDNvefKoBwLsxpwKAIzaw")
    OWNER_ID = list(map(int, getenv("OWNER_ID", "5042510749").split()))
    

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

