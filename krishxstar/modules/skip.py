# --------------------------------------------------------------------------------
#  KrishXStarMusic © 2026
#  Developed by KRISH X STAR CODER ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------

import asyncio

from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message

from KrishXStarMusic import bot, call_py
from KrishXStarMusic.core.player import play_song
from KrishXStarMusic.core.queue import peek_current, pop_current, queue_size
from KrishXStarMusic.utils.formatters import short
from KrishXStarMusic.utils.helpers import delete_file
from KrishXStarMusic.utils.permissions import is_user_authorized


# ─────────────────────────────────────────────
# SKIP SONG
# ─────────────────────────────────────────────
@bot.on_message(filters.group & filters.command("skip"))
async def skip_cmd(_, message: Message) -> None:

    chat_id = message.chat.id

    # Admin Check
    if not await is_user_authorized(message):
        await message.reply(
            "<b>❍ Admin Only</b>\n<b>❍ This command is for group admins.</b>",
            parse_mode=ParseMode.HTML,
        )
        return

    # Queue Check
    if not queue_size(chat_id):
        await message.reply(
            "<b>❍ Queue is empty</b>\n<b>❍ No songs to skip.</b>",
            parse_mode=ParseMode.HTML,
        )
        return

    # Skipping Message
    sm = await message.reply(
        "<b>❍ Skipping current track...</b>",
        parse_mode=ParseMode.HTML,
    )

    # Remove Current Song
    skipped = pop_current(chat_id)

    # Leave Current Stream
    try:
        await call_py.leave_call(chat_id)
    except Exception:
        pass

    # Cleanup
    await asyncio.sleep(2)
    try:
        delete_file(skipped.get("file_path", ""))
    except Exception:
        pass

    # Next Song
    nxt = peek_current(chat_id)

    if nxt:
        await sm.edit_text(
            f"<b>❍ Skipped Track :</b><code>{short(skipped['title'])}</code>\n"
            f"<b>❍ Now Playing :</b>\n<code>{nxt['title']}</code>",
            parse_mode=ParseMode.HTML,
        )

        dm = await bot.send_message(
            chat_id,
            f"<b>❍ Next Track :</b><code>{nxt['title']}</code>",
            parse_mode=ParseMode.HTML,
        )

        await play_song(chat_id, dm, nxt)

    else:
        await sm.edit_text(
            f"<b>❍ Skipped Track :</b><code>{short(skipped['title'])}</code>\n"
            f"<b>❍ Queue is now empty</b>",
            parse_mode=ParseMode.HTML,
        )
