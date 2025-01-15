# Don't remove This Line From Here. Tg: @rohit_1888 | @Javpostr

import asyncio
import tempfile
import base64
import os
from telethon.errors import FloodWait
from datetime import datetime
from pyrogram import filters, Client, enums
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatAction
from bot import Bot
from config import *
from database.database import *
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
    'status', 'req_fsub', 'myplan', 'login', 'header', 'footer', 'save'
]))

async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Please Wait...!", quote=True)
    try:
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id=client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong..!")
        return

    converted_id = post_message.id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    
    # Assuming encode is a regular function and not async
    base64_string = encode(string)  # No await needed here
    link = f"https://telegram.me/{client.username}?start={base64_string}"

    string = f"get-{converted_id}"
    string = string.replace("get-", "premium-")
    
    # No await here as well
    base64_string = encode(string)  # No await needed
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



@Bot.on_message(filters.private & is_admin & ~filters.command('save'))
async def fetch_and_upload_content(client: Client, message: Message):
    """Fetches restricted content, processes it, and uploads it with header and footer."""
    
    # Ask the user to send a valid link
    await message.reply_text("Please send the link to proceed (within 30 seconds):")

    try:
        # Set timeout for 30 seconds
        response_message = await client.wait_for_message(
            chat_id=message.chat.id, 
            timeout=30,  # Timeout in seconds
            filters=filters.text
        )
        
        # Extract the link from the user's response
        link = None
        if "https://t.me/" in (response_message.text or ""):
            link = next((word for word in response_message.text.split() if "https://t.me/" in word and "?start=" in word), None)

        if not link:
            return await message.reply_text("Invalid link! Please make sure the link is correct and contains '?start='.")

        # Parse the link
        link_parts = link.split("?start=")
        bot_username = link_parts[0].split("/")[-1]
        start_param = link_parts[1] if len(link_parts) > 1 else None

        # Retrieve session
        user_session = await db.get_session(message.from_user.id)
        if not user_session:
            return await message.reply_text("You need to /login first to fetch content.")

        # Start client session
        acc = Client("restricted_content", session_string=user_session, api_id=API_ID, api_hash=API_HASH)
        await acc.start()

        # Send /start command
        sent_message = await acc.send_message(bot_username, f"/start {start_param}" if start_param else "/start")

        # Wait and fetch the latest messages
        await asyncio.sleep(10)
        messages = []
        async for response in acc.get_chat_history(bot_username, limit=100):
            if response.date > sent_message.date:
                msg_type = get_message_type(response)
                if msg_type:
                    messages.append((msg_type, response))

        if not messages:
            return await message.reply_text("No new messages received after sending the link.")

        # Process and upload messages
        uploaded_links = []
        message_ids = []
        for msg_type, response in messages:
            db_msg = await process_and_upload(client, acc, msg_type, response)
            if db_msg:
                uploaded_links.append(f"https://t.me/c/{str(abs(DB_CHANNEL))}/{db_msg.id}")
                message_ids.append(db_msg.id)

        # Generate encoded link
        if uploaded_links:
            if len(message_ids) == 1:
                converted_id = message_ids[0] * abs(client.db_channel.id)
                string = f"get-{converted_id}"
            else:
                f_msg_id = message_ids[0] * abs(client.db_channel.id)
                s_msg_id = message_ids[-1] * abs(client.db_channel.id) if len(message_ids) > 1 else 0
                string = f"get-{f_msg_id}-{s_msg_id}"

            base64_string = encode(string)
            new_link = f"https://t.me/{client.username}?start={base64_string}"

            # Fetch header and footer from the database
            header = await db.get_header(message.from_user.id) or ""
            footer = await db.get_footer(message.from_user.id) or ""

            # Combine header, link, and footer
            final_message = f"{header}\n\n<b>Your content has been processed successfully:</b>\n{new_link}\n\n{footer}"

            # Replace only the link in the caption
            if message.caption:  # For photo messages with captions
                updated_caption = f"{header}\n\n{message.caption.replace(link, new_link)}\n\n{footer}"
                await message.reply_photo(
                    photo=message.photo.file_id,
                    caption=updated_caption,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🔗 Share Link", url=f'https://telegram.me/share/url?url={new_link}')]
                    ])
                )
            else:  # For text messages or captions without a photo
                reply_markup = InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔗 Share Link", url=f'https://telegram.me/share/url?url={new_link}')]
                ])
                await message.reply_text(
                    final_message,
                    reply_markup=reply_markup,
                    disable_web_page_preview=True,
                )
        else:  # No uploaded links; handle with header and footer
            header = await db.get_header(message.from_user.id) or ""
            footer = await db.get_footer(message.from_user.id) or ""
            no_content_message = f"{header}\n\n<b>No new content was fetched after processing your link.</b>\n\n{footer}"
            await message.reply_text(no_content_message)

    except asyncio.TimeoutError:
        # If the user doesn't respond within 30 seconds
        await message.reply_text("You took too long to send the link. Please try again.")

    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

    finally:
        # Ensure to stop the client session if it was started
        if 'acc' in locals():
            await acc.stop()