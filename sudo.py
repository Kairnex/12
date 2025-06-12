import os
from pyrogram import filters
from pyrogram.types import Message
from config import SUDO_USERS
from utils.db import users_col

def register(app):
    sudo_filter = filters.user(SUDO_USERS)

    @app.on_message(filters.command("broadcast") & sudo_filter)
    async def broadcast(_, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a message to broadcast.")
        count = 0
        for chat in users_col.find():
            try:
                await app.copy_message(chat_id=chat["user_id"], from_chat_id=message.chat.id, message_id=message.reply_to_message.id)
                count += 1
            except:
                continue
        await message.reply(f"✅ Broadcasted to {count} users.")

    @app.on_message(filters.command("restart") & sudo_filter)
    async def restart(_, message: Message):
        await message.reply("♻️ Restarting...")
        os.execv(sys.executable, ["python"] + sys.argv)
