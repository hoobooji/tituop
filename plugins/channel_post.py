# Don't remove This Line From Here. Tg: @im_piro | @PiroHackz

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import OWNER_ID, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import *


DB_CHANNEL = CHANNEL_ID
FILE_SIZE_LIMIT = 1 * 1024 * 1024 * 1024  # 1GB limit


def encode(data: str) -> str:
    """Encodes the input data into a base64 format with stripped padding."""
    encoded = base64.urlsafe_b64encode(data.encode("utf-8")).decode("utf-8")
    return encoded.strip("=")  # Strip padding for cleaner URLs


async def decode(base64_string: str) -> list:
    """Decodes a base64 string and returns a list of message IDs."""
    base64_string = base64_string.strip("=")
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string = base64.urlsafe_b64decode(base64_bytes).decode("utf-8")

    # Parse the string to extract message IDs
    if string.startswith("get-"):
        ids = string[4:].split(",")
        return [int(msg_id) for msg_id in ids]  # Convert IDs back to integers
    return []


@Bot.on_message(filters.private & is_admin & ~filters.command([
    'start', 'users', 'broadcast', 'batch', 'genlink', 'stats', 'addpaid', 'removepaid', 'listpaid',
    'help', 'cmd', 'info', 'add_fsub', 'fsub_chnl', 'restart', 'del_fsub', 'add_admins', 'del_admins', 
    'admin_list', 'cancel', 'auto_del', 'forcesub', 'files', 'add_banuser', 'token', 'del_banuser', 'banuser_list', 
    'status', 'req_fsub', 'myplan'
]))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote = True)
    try:
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return
    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://telegram.me/{client.username}?start={base64_string}"

    string = f"get-{converted_id}"
    string = string.replace("get-", "premium-")
    base64_string = await encode(string)
    link1 = f"https://telegram.me/{client.username}?start={base64_string}"

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Public Link", url=link)],
            [InlineKeyboardButton("Premium User", url=link1)]
        ]
    )

    await reply_text.edit(
        "<b>> Your Links</b>",
        disable_web_page_preview=True,
        reply_markup=keyboard
    )

# Don't remove This Line From Here. Tg: @im_piro | @PiroHackz
