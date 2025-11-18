# ===========================
# ⚙️ CONFIGURATION FILE
# ===========================

import os

# BASIC BOT SETTINGS
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBitz")
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@BackupDummy")

START_CREDITS = 10

# API LINKS
MOBILE_API = os.getenv("API_MOBILE", "https://ph-ng-pi.vercel.app/?number=")
PINCODE_API = os.getenv("API_PINCODE", "https://pincode-ng.vercel.app/lookup?pincode=")
RC_API = os.getenv("API_VEHICLE", "https://vvvin-ng.vercel.app/lookup?rc=")
IMEI_API = os.getenv("API_IMEI", "https://ng-imei-info.vercel.app/?imei_num=")

GST_API = ""
IFSC_API = ""

# Coming soon
COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Passport Lookup",
    "Email OSINT",
    "Voter ID Lookup"
]

# Button text required by handlers
BACK = "🔙 Back"
SEARCH = "🔎 Search"
CHECK = "✔️ Check Status"

PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "")
OWNER_USER = os.getenv("OWNER_USER", "@AbdulBitz")
