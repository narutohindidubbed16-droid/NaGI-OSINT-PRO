# ============================
# 📌 database.py
# MongoDB User & Referral System
# ============================

import os
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["NagiOSINT"]
users = db["users"]

DEFAULT_CREDITS = 10


# ============================
# CREATE USER
# ============================
def create_user(user_id, username, firstname):
    u = users.find_one({"user_id": user_id})

    if u:
        return False  # user already exists

    users.insert_one({
        "user_id": user_id,
        "username": username,
        "firstname": firstname,
        "credits": DEFAULT_CREDITS,
        "referrals": []
    })

    return True


# ============================
# GET CREDITS
# ============================
def get_user_credits(user_id):
    u = users.find_one({"user_id": user_id})
    if not u:
        return DEFAULT_CREDITS
    return u.get("credits", DEFAULT_CREDITS)


# ============================
# DECREASE CREDIT
# ============================
def decrease_credit(user_id):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"credits": -1}}
    )


# ============================
# ADD REFERRAL
# ============================
def add_referral(referrer_id, new_user_id):
    users.update_one(
        {"user_id": referrer_id},
        {
            "$push": {"referrals": new_user_id},
            "$inc": {"credits": 1}   # +1 credit reward
        }
    )
