import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "ImTharuk")
ALIVE_NAME = getenv("ALIVE_NAME", "SL Bots")
BOT_USERNAME = getenv("BOT_USERNAME", "videostreamslbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SLBotsofficialHelp")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "trtechguide")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SLBotsOfficial")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/8940cebd9b7f37d0c259e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TharukRenuja/VStream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/37367475c36aa27c7ffaf.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/38f196966b409f8c51442.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/e7ac9dfffcf34cfccb5da.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/3c8879584e9a0d3ed74ec.jpg")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "Client0")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
