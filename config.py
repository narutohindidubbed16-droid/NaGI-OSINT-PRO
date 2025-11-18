# ===========================
# ⚙️ CONFIGURATION FILE
# ===========================

import os

# BASIC BOT SETTINGS
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

# Channel controls
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBitz")
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@BackupDummy")

# Credits
START_CREDITS = 10

# API LINKS (Match exactly with handlers.py)
MOBILE_API = os.getenv("API_MOBILE", "https://ph-ng-pi.vercel.app/?number=")
PINCODE_API = os.getenv("API_PINCODE", "https://pincode-ng.vercel.app/lookup?pincode=")
RC_API = os.getenv("API_VEHICLE", "https://vvvin-ng.vercel.app/lookup?rc=")
IMEI_API = os.getenv("API_IMEI", "https://ng-imei-info.vercel.app/?imei_num=")

# These must exist (handlers.py imports them)
GST_API = os.getenv("API_GST", "")
IFSC_API = os.getenv("API_IFSC", "")

# Coming soon
COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Passport Lookup",
    "Email OSINT",
    "Voter ID Lookup"
]

# Button text required by handlers & keyboards
BACK = "🔙 Back"
SEARCH = "🔎 Search"
CHECK = "✔️ Check Status"

# Private invite & owner
PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "")
OWNER_USER = os.getenv("OWNER_USER", "@AbdulBotz")
