# ===========================
# CONFIG.PY (FINAL)
# ===========================

import os

BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_NAME = "Nagi OSINT PRO"
BOT_TOKEN = os.getenv("TOKEN")

MAIN_CHANNEL = os.getenv("MAIN_CHANNEL")      # Only public channel
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")  # Private ok

PRIVATE_INVITE = os.getenv("PRIVATE_INVITE")

# ==========================
# OTHER SETTINGS
# ==========================

START_CREDITS = 5   # Required for handlers.py

COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Voter ID Lookup",
    "Passport Lookup",
    "Email OSINT",
]

BOLD = "𝗕𝗢𝗟𝗗"
CHECK = "✔️"
CROSS = "❌"
LOCK = "🔐"
SEARCH = "🔎"
BACK = "🔙"        # Required for keyboards.py

# ==========================
# API LINKS
# ==========================

MOBILE_API = os.getenv("API_MOBILE")
RC_API = os.getenv("API_VEHICLE")
PINCODE_API = os.getenv("API_PINCODE")
IMEI_API = os.getenv("API_IMEI")
GST_API = os.getenv("API_GST")
IFSC_API = os.getenv("API_IFSC")
