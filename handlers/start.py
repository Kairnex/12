
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.db import save_user

def register(app):
    @app.on_message(filters.command("start"))
    async def start_handler(_, message: Message):
        if message.chat.type != "private":
            return
        save_user(message.from_user.id)
        await message.reply(
            "**👋 Welcome to EditWatcherBot!**\n\n"
            "- Deletes edited messages\n"
            "- Detects NSFW content\n"
            "- Auto-cleans messages\n"
            "- Use in groups only.\n\n"
            "__Add me to your group to start!__",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Support", url="https://t.me/your_support_group")],
                [InlineKeyboardButton("Add to Group", url=f"https://t.me/{(await app.get_me()).username}?startgroup=true")]
            ])
        )
# Placeholder for start.py
