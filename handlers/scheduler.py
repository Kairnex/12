
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from utils.db import is_user_authorized
from utils.nsfw import download_and_check

def register(app):
    @app.on_edited_message(filters.group)
    async def delete_edits(app, message: Message):
        try:
            member = await app.get_chat_member(message.chat.id, message.from_user.id)
            if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
            if is_user_authorized(message.chat.id, message.from_user.id):
                return
            await message.delete()
        except Exception as e:
            print(f"[EDIT DELETE ERROR] {e}")

    @app.on_message(filters.group & (filters.photo | filters.video | filters.document))
    async def filter_nsfw_media(app, message: Message):
        try:
            if await download_and_check(app, message):
                await message.delete()
        except Exception as e:
            print(f"[NSFW MEDIA DELETE ERROR] {e}")

    @app.on_message(filters.group & filters.text)
    async def filter_nsfw_text(app, message: Message):
        NSFW_KEYWORDS = ["porn", "sex", "nude", "boobs", "xxx"]
        try:
            if any(word in message.text.lower() for word in NSFW_KEYWORDS):
                member = await app.get_chat_member(message.chat.id, message.from_user.id)
                if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                    await message.delete()
        except Exception as e:
            print(f"[NSFW TEXT DELETE ERROR] {e}")
