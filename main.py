# ========================================================
# KRISH X STAR CODER - Main File
# ========================================================

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "KrishXStarBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    print("🚀 KRISH X STAR CODER Bot Started 🚀")
    print("Support: https://t.me/KRISH_HACKER_OP")
    app.run()
