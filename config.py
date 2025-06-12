import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://codexkairnex:gm6xSxXfRkusMIug@cluster0.bplk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7758785176:AAGqM9GnLngx0Uv5zKg13Pr0UsBEoHTV_S8")
API_ID = int(os.getenv("API_ID", "21189715"))
API_HASH = os.getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")

SUDO_USERS = [7416620797, 6999372290]  # Replace with real user IDs
