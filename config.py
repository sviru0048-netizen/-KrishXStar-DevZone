import os
import re
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables (local testing ke liye)
load_dotenv()

# ======================================================
API_ID = int(os.getenv("API_ID", "31533046"))
API_HASH = os.getenv("API_HASH", "4f0f99c64d8e82a490c42a7faaa36710")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8754634148:AAGSXbkDIkMcwNiHO-EiMspmgUaemVBlXE")

OWNER_ID = int(os.getenv("OWNER_ID", "7526566458"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "KRISH_HACKER_OWNER")
BOT_USERNAME = os.getenv("BOT_USERNAME", "KrishXStarBot")
BOT_NAME = os.getenv("BOT_NAME", "KRISH X STAR CODER")
ASSUSERNAME = os.getenv("ASSUSERNAME")

# ======================================================
MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)  # MongoDB Atlas URI
LOGGER_ID = int(os.getenv("LOGGER_ID", "-1002060224175"))

BASE_URL = os.getenv("API_URL", "https://BabyAPI.Pro")
API_KEY = os.getenv("API_KEY", "ADMINBABYX20F56755E70E0694DDCC844F5F1BB465")

# ======================================================
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "17000"))
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "25"))
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "9000"))

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/KrishXStar-DevZone")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/KRISH_HACKER_OP")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/KRISH_HACKER_OP")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")

# ======================================================
# String Sessions (Assistant accounts)
STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)
STRING6 = os.getenv("STRING_SESSION6", None)
STRING7 = os.getenv("STRING_SESSION7", None)

# ======================================================
# Images
START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/j5y9f6.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/j5y9f6.jpg")

PLAYLIST_IMG_URL = "https://files.catbox.moe/b0e4vk.jpg"
STATS_IMG_URL = "https://files.catbox.moe/psya34.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/2y5o3g.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

# ======================================================
# Filters and Admins
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ======================================================
# Helper function
def time_to_seconds(time: str) -> int:
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ======================================================
# Validation
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. It must start with https://")

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. It must start with https://")
