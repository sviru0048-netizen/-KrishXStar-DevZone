# --------------------------------------------------------------------------------
#  KrishXStarMusic © 2026
#  Developed by KRISH X STAR CODER ❤️
#
#  Unauthorized copying, editing, re-uploading or removing credits
#  from this source code is strictly prohibited.
# --------------------------------------------------------------------------------

import asyncio

from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import config
from KrishXStarMusic import bot, call_py
from KrishXStarMusic.core.call import leave_vc
from KrishXStarMusic.core.player import play_song
from KrishXStarMusic.core.queue import clear_queue, peek_current, pop_current, queue_size
from KrishXStarMusic.utils.formatters import short
from KrishXStarMusic.utils.helpers import delete_file
from KrishXStarMusic.utils.permissions import is_user_authorized


@bot.on_callback_query()
async def on_callback(client, cbq: CallbackQuery) -> None:

    chat_id = cbq.message.chat.id
    user = cbq.from_user
    data = cbq.data

    # ── Admin Check ──────────────────────────
    if data in ("pause", "resume", "skip", "stop", "clear"):
        if not await is_user_authorized(cbq):
            await cbq.answer("❍ Admins Only", show_alert=True)
            return

    # ─────────────────────────────────────────
    # PAUSE
    # ─────────────────────────────────────────
    if data == "pause":
        try:
            await call_py.pause(chat_id)
            await cbq.answer("Paused")
            await client.send_message(
                chat_id,
                f"<b>❍ Stream Paused</b>\n<b>❍ By :</b> {user.mention}",
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            await cbq.answer("Failed To Pause", show_alert=True)

    # ─────────────────────────────────────────
    # RESUME
    # ─────────────────────────────────────────
    elif data == "resume":
        try:
            await call_py.resume(chat_id)
            await cbq.answer("Resumed")
            await client.send_message(
                chat_id,
                f"<b>❍ Stream Resumed</b>\n<b>❍ By :</b> {user.mention}",
                parse_mode=ParseMode.HTML,
            )
        except Exception:
            await cbq.answer("Failed To Resume", show_alert=True)

    # ─────────────────────────────────────────
    # SKIP
    # ─────────────────────────────────────────
    elif data == "skip":
        if not queue_size(chat_id):
            await cbq.answer("Queue Is Empty", show_alert=True)
            return

        skipped = pop_current(chat_id)
        try:
            await call_py.leave_call(chat_id)
        except Exception:
            pass

        await asyncio.sleep(2)

        try:
            delete_file(skipped.get("file_path", ""))
        except Exception:
            pass

        await client.send_message(
            chat_id,
            f"<b>❍ Track Skipped</b>\n<b>❍ By :</b> {user.mention}\n<b>❍ Song :</b><code>{short(skipped['title'])}</code>",
            parse_mode=ParseMode.HTML,
        )

        nxt = peek_current(chat_id)
        if nxt:
            await cbq.answer("Playing Next")
            dm = await bot.send_message(
                chat_id,
                f"<b>❍ Next Track :</b><code>{nxt['title']}</code>",
                parse_mode=ParseMode.HTML,
            )
            await play_song(chat_id, dm, nxt)
        else:
            await cbq.answer("Queue Empty", show_alert=True)

    # ─────────────────────────────────────────
    # STOP
    # ─────────────────────────────────────────
    elif data == "stop":
        await leave_vc(chat_id)
        await cbq.answer("Stopped")
        await client.send_message(
            chat_id,
            f"<b>❍ Playback Stopped</b>\n<b>❍ By :</b> {user.mention}",
            parse_mode=ParseMode.HTML,
        )

    # ─────────────────────────────────────────
    # CLEAR
    # ─────────────────────────────────────────
    elif data == "clear":
        clear_queue(chat_id)
        await cbq.answer("Queue Cleared")
        await cbq.message.edit_text(
            f"<b>❍ Queue Cleared</b>\n<b>❍ By :</b> {user.mention}",
            parse_mode=ParseMode.HTML,
        )

    elif data == "noop":
        await cbq.answer()

    elif data == "show_help":
        await _show_help(cbq)

    elif data == "go_back":
        await _go_back(cbq)

    elif data.startswith("help_"):
        await _help_section(cbq, data)


# ── Help pages ────────────────────────────────────────────────────────────────

async def _go_back(cbq: CallbackQuery) -> None:
    uid  = cbq.from_user.id
    name = cbq.from_user.first_name or "User"
    caption = (
        "<b>╭────────────────────▣</b>\n"
        f"<b>│❍ Hey</b> <a href='tg://user?id={uid}'>{name}</a>, 🥀\n"
        f"<b>│❍ This is {config.BOT_NAME} !</b>\n"
        "<b>├────────────────────▣</b>\n"
        "<b>│❍ A fast & powerful Telegram Music Bot.</b>\n"
        "<b>├────────────────────▣</b>\n"
        f"<b>│❍ Powered By » KRISH X STAR CODER</b>\n"
        "<b>╰────────────────────▣</b>"
    )
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("⛩️ Add Me Baby ⛩️", url=f"{config.BOT_LINK}?startgroup=true")],
        [
            InlineKeyboardButton("🍬 Support 🍬", url=config.SUPPORT_GROUP),
            InlineKeyboardButton("🍹 Update 🍹",   url=config.UPDATES_CHANNEL),
        ],
        [InlineKeyboardButton("🏩 Help & Commands 🏩", callback_data="show_help")],
        [
            InlineKeyboardButton("🫧 Owner 🫧",  url=f"tg://user?id={config.OWNER_ID}"),
            InlineKeyboardButton("🍡 Source 🍡", url="https://github.com"),
        ],
    ])
    await cbq.message.edit_caption(caption=caption, parse_mode=ParseMode.HTML, reply_markup=kb)


async def _show_help(cbq: CallbackQuery) -> None:
    kb = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("❍ Play ❍",   callback_data="help_music"),
            InlineKeyboardButton("❍ Utility ❍", callback_data="help_util"),
        ],
        [InlineKeyboardButton("⌯ Home ⌯",    callback_data="go_back")],
        ])
    await cbq.message.edit_text(
        "<b>📜 Choose a category :</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=kb,
    )


async def _help_section(cbq: CallbackQuery, data: str) -> None:
    back = InlineKeyboardMarkup([[InlineKeyboardButton("⌯ Back ⌯", callback_data="show_help")]])
    texts = {
        "help_music": (
            "<b>╭────────────────────▣</b>\n"
            "<b>│🎵 Music Commands</b>\n"
            "<b>├────────────────────▣</b>\n"
            "<b>│❍ /play</b> <song or URL>\n"
            "<b>│❍ /pause</b>  — Pause  <i>(Admin)</i>\n"
            "<b>│❍ /resume</b> — Resume <i>(Admin)</i>\n"
            "<b>│❍ /skip</b>   — Skip   <i>(Admin)</i>\n"
            "<b>│❍ /stop</b>   — Stop   <i>(Admin)</i>\n"
            "<b>│❍ /clear</b>  — Clear Queue <i>(Admin)</i>\n"
            "<b>╰────────────────────▣</b>"
        ),
        "help_util": (
            "<b>╭────────────────────▣</b>\n"
            "<b>│🔍 Utility</b>\n"
            "<b>├────────────────────▣</b>\n"
            "<b>│❍ /ping</b>   — Stats & Latency\n"
            "<b>│❍ /speedtest</b>  — Network Speed Test\n"
            "<b>│❍ /spt</b>        — Shortcut for Speedtest\n"
            "<b>│❍ /reboot</b> — Reset Chat State\n"
            f"<b>│❍ Max Song: {config.MAX_DURATION_SECONDS // 60} minutes</b>\n"
            "<b>╰────────────────────▣</b>"
        ),
    }
    await cbq.message.edit_text
