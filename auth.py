from pyrogram import filters
from pyrogram.types import Message
from utils.db import add_authorized_user, remove_authorized_user, get_auth_users
from pyrogram.enums import ChatMemberStatus

def register(app):
    @app.on_message(filters.command("auth") & filters.group)
    async def auth_user(_, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a user to authorize.")
        member = await message.chat.get_member(message.from_user.id)
        if member.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return await message.reply("Only admins can authorize users.")
        add_authorized_user(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("User authorized successfully.")

    @app.on_message(filters.command("unauth") & filters.group)
    async def unauth_user(_, message: Message):
        if not message.reply_to_message:
            return await message.reply("Reply to a user to unauthorize.")
        remove_authorized_user(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("User unauthorized successfully.")

    @app.on_message(filters.command("authlist") & filters.group)
    async def list_auth(_, message: Message):
        auths = get_auth_users(message.chat.id)
        if not auths:
            return await message.reply("No authorized users.")
        mentions = [f"- `{user}`" for user in auths]
        await message.reply("**Authorized Users:**\n" + "\n".join(mentions))
