
import asyncio
from pyrogram import Client
from pyrogram.enums import MessageMediaType

def register(app: Client):
    async def auto_clean():
        while True:
            async for dialog in app.get_dialogs():
                if dialog.chat.type == "supergroup":
                    await app.delete_messages(dialog.chat.id, range(dialog.top_message_id - 200, dialog.top_message_id), revoke=True)
            await asyncio.sleep(86400)  # 24 hours

    async def auto_clean_media():
        while True:
            async for dialog in app.get_dialogs():
                if dialog.chat.type == "supergroup":
                    async for msg in app.get_chat_history(dialog.chat.id, limit=100):
                        if msg.media:
                            await app.delete_messages(dialog.chat.id, msg.id)
            await asyncio.sleep(7200)  # 2 hours

    app.loop.create_task(auto_clean())
    app.loop.create_task(auto_clean_media())
