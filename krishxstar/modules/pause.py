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
# PAUSE STREAM
# ─────────────────────────────────────────────
@bot.on_message(filters.group & filters.command("pause"))
async def pause_cmd(_, message: Message) -> None:

    # Admin Check
    if not await is_user_authorized(message):
        await message.reply(
            "<b>❍ Admin Only</b>\n<b>❍ This command is for group admins.</b>",
            parse_mode=ParseMode.HTML,
        )
        return

    # Pause Stream
    try:
        await call_py.pause(message.chat.id)
        await message.reply(
            "<b>❍ Stream Paused</b>\n<b>❍ Music playback temporarily stopped.</b>",
            parse_mode=ParseMode.HTML,
        )
    except Exception as e:
        await message.reply(
            f"<b>❍ Pause Failed</b> <code>{e}</code>",
            parse_mode=ParseMode.HTML,
        )
