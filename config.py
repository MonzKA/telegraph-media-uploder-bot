import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
 
BOT_TOKEN = getenv("5710006787:AAH4XE2dKG_A3ekHr-4bOBVjFBepZvKudQ8") 
API_ID = int(getenv("14401954"))
API_HASH = getenv("c342aca287037f205a0dcbe8c7d82579")
 
