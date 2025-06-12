# handlers/moderation.py

from pyrogram import filters
from pyrogram.types import Message
from utils.db import is_auth_user, add_warning, get_warning_count, reset_warnings
from utils.helpers import is_admin
from utils.media_check import is_nsfw_content


def register(app):
    @app.on_edited_message(filters.group)
    async def edited_message_handler(client, message: Message):
        try:
            if await is_admin(message.chat.id, message.from_user.id):
                return  # Don't delete edits from admins

            if await is_auth_user(message.chat.id, message.from_user.id):
                return  # Don't delete edits from authorized users

            await message.delete()
        except Exception as e:
            print(f"Error deleting edited message: {e}")

    @app.on_message(filters.group & filters.media)
    async def media_check_handler(client, message: Message):
        try:
            if await is_admin(message.chat.id, message.from_user.id):
                return  # Skip admins

            if await is_auth_user(message.chat.id, message.from_user.id):
                return  # Skip authorized users

            if await is_nsfw_content(message):
                await message.delete()
                await message.reply_text("⚠️ NSFW content is not allowed here.")
        except Exception as e:
            print(f"Error in media check: {e}")
