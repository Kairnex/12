from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client["editwatcherbot"]

users_col = db["users"]
auth_col = db["auth_users"]
groups_col = db["groups"]

def save_user(user_id: int):
    users_col.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

def is_user_authorized(group_id, user_id):
    return auth_col.find_one({"group_id": group_id, "user_id": user_id}) is not None

def add_authorized_user(group_id, user_id):
    auth_col.update_one({"group_id": group_id, "user_id": user_id}, {"$set": {"group_id": group_id, "user_id": user_id}}, upsert=True)

def remove_authorized_user(group_id, user_id):
    auth_col.delete_one({"group_id": group_id, "user_id": user_id})

def get_auth_users(group_id):
    return [doc["user_id"] for doc in auth_col.find({"group_id": group_id})]
