## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu6PhAxbYigoxaHp183YT87JindH3mwRGu9OT7_ev6ScrRUTj0hIvmmMwvpRF9MTFssmvtkWoAK116rlr7QD2NygK_DDN6e6qXfyPAsc_t8_ozL7396iJgRC1Fj5EDN1un89pBdWQQ9EC-HeRqD9wianF4kc7_6Td9JOWw0L5Yk7SYvLzotpq0Lh4gPNjKLJ5Rnp8iZqcdFKv4mqYFSA6fwzAEjHHKTM5gKoJwuUzniI10mugMFxk8Hxy6dMQeuI-0Q6jDiJKwTAFRj3gqAsSO7PbMa090CawE4QQtfuUh6oe3AhDPw80O7ybVLRGd42xmJuY5ngF4PHuWmS6yUXUSMo=")
BOT_TOKEN = getenv("BOT_TOKEN", "5566177735:AAERlp-uFp8PGFr3gk6CJW_Qylssil4cEcY")
BOT_NAME = getenv("BOT_NAME", "mjkb")
API_ID = int(getenv("API_ID", "17351403"))
API_HASH = getenv("API_HASH", "43ff26233f2b94e70048748ae2ab8d99")
OWNER_NAME = getenv("OWNER_NAME", "m19v1")
OWNER_USERNAME = getenv("OWNER_USERNAME", "mu12_14BOT")
ALIVE_NAME = getenv("ALIVE_NAME", "mumtaz")
BOT_USERNAME = getenv("BOT_USERNAME", "mu12_14BOT")
OWNER_ID = getenv("OWNER_ID", "5181284590")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "m12gm")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mmvhgb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mmvhgb")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5181284590").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
