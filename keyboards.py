# ===============================
# 📌 keyboards.py
# All Inline Keyboards & Buttons
# ===============================

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import MAIN_CHANNEL, BACKUP_CHANNEL, COMING_SOON_LIST, BACK, SEARCH, CHECK


# ===============================
# REQUIRED CHANNEL JOIN CHECK UI
# ===============================
def join_channels_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 Join Main Channel", url=f"https://t.me/{MAIN_CHANNEL.replace('@','')}"),
        ],
        [
            InlineKeyboardButton("🛡 Join Backup Channel", url=f"https://t.me/{BACKUP_CHANNEL.replace('@','')}"),
        ],
        [
            InlineKeyboardButton(f"{CHECK} I have Joined", callback_data="verify_join")
        ]
    ])


# ===============================
# MAIN MENU UI (Same as screenshot)
# ===============================
def main_menu_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📱 Mobile Lookup", callback_data="mobile_lookup"),
            InlineKeyboardButton("🚗 RC Lookup", callback_data="rc_lookup"),
        ],
        [
            InlineKeyboardButton("📦 Pincode Info", callback_data="pincode_lookup"),
            InlineKeyboardButton("🏦 IFSC Search", callback_data="ifsc_lookup"),
        ],
        [
            InlineKeyboardButton("🧾 GST Lookup", callback_data="gst_lookup"),
            InlineKeyboardButton("📡 IMEI Lookup", callback_data="imei_lookup"),
        ],
        [
            InlineKeyboardButton("🎁 Refer & Earn", callback_data="refer"),
        ],
        [
            InlineKeyboardButton("⚙️ Coming Soon", callback_data="coming_soon"),
        ]
    ])


# ===============================
# INPUT PANEL (after user clicks)
# ===============================
def ask_input_kb():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"{BACK} Back to Menu", callback_data="back_home")
        ]
    ])


# ===============================
# COMING SOON UI
# ===============================
def coming_soon_kb():
    buttons = []
    for item in COMING_SOON_LIST:
        buttons.append([InlineKeyboardButton(f"🚧 {item}", callback_data="na")])

    buttons.append([InlineKeyboardButton(f"{BACK} Back", callback_data="back_home")])

    return InlineKeyboardMarkup(buttons)
