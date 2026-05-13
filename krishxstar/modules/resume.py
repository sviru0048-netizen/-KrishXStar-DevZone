# --------------------------------------------------------------------------------
#  KrishXStarMusic © 2026
#  Developed by KRISH X STAR CODER ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from KrishXStarMusic import bot, call_py
from KrishXStarMusic.utils.permissions import is_user_authorized


# ─────────────────────────────────────────────
# RESUME STREAM
# ─────────────────────────────────────────────
@bot.on_message(filters.group & filters.command("resume"))
async def resume_cmd(_, message: Message) -> None:

    # Admin Check
    if not await is_user_authorized(message):
        await message.reply(
            "<b>❍ Admin Only</b>\n<b>❍ This command is for group admins.</b>",
            parse_mode=ParseMode.HTML,
        )
        return

    # Resume Stream
    try:
        await call_py.resume(message.chat.id)
        await message.reply(
            "<b>❍ Stream Resumed</b>\n<b>❍ Music playback continued.</b>",
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        await message.reply(
            f"<b>❍ Resume Failed</b> <code>{e}</code>",
            parse_mode=ParseMode.HTML,
      )
