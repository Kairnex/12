import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

SUDO_USERS = [123456789, 987654321]  # Replace with real user IDs
