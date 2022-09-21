## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAdm1kR3tiV8XzrO7_HGM581Kv8901PGth1HqmJBEHA2bx_ehdYLgPRTw2D9uZpH9EurYDC7xUWe9ptD7oLTEBXDu7t1wub1Z-5EvcERdsEEDIR4yWguVGfZPs41wU4YvaLhQ9f514imHQ9gCaCoBEMnfGhoY8Wch9A0kfojj0VcWmWqdPLIIyiztF8Mwjxce41QH0pZDUpoS9x993EloLBu6miniDFk_7AsuYFQuLLXHICCxaIwGjjdI-s5n_RicPNAI3aesSqmKdKjjbsICHqDfOPHYDLEhOye_aOmbQS90P-FM5oua858XrR-GjPOJIELlYn62AgPOWRbNuGa3ECAAAAATE996MA")
BOT_TOKEN = getenv("BOT_TOKEN", "5654516125:AAH42HMgV_mkEeI_C-IsCLRQ6ROokGY0pdI")
BOT_NAME = getenv("BOT_NAME", "imamhussanbot")
API_ID = int(getenv("API_ID", "15492696"))
API_HASH = getenv("API_HASH", "8758d4e677d9b01c414ed1a3143ac0b3")
OWNER_NAME = getenv("OWNER_NAME", "LOLE")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Folw_Azer")
ALIVE_NAME = getenv("ALIVE_NAME", "LOLE")
BOT_USERNAME = getenv("imamhussanbot", "")
OWNER_ID = getenv("OWNER_ID", "5121111971")
ASSISTANT_NAME = getenv("Folw_Azer", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
