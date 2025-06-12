from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import start, auth, moderation, sudo, scheduler

app = Client("editwatcherbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

start.register(app)
auth.register(app)
moderation.register(app)
sudo.register(app)
scheduler.register(app)

print("✅ Bot is running...")
app.run()
