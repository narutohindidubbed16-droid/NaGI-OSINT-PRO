# ===========================
# ⚙️ CONFIGURATION FILE
# ===========================

import os

# ===========================
# BOT BASIC SETTINGS
# ===========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

# Required channels
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBotz")   # Public main channel
PUBLIC_CHANNEL = os.getenv("PUBLIC_CHANNEL", "@AbdulBotz")  # Same as main if needed
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@darknagibackup")  # Private backup

# Private invite (extra)
PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "")

# Owner
OWNER_USER = os.getenv("OWNER_USER", "@AbdulBotz")

# ===========================
# USER CREDITS
# ===========================

START_CREDITS = 10


# ===========================
# API LINKS
# ===========================

MOBILE_API = os.getenv("API_MOBILE", "https://ph-ng-pi.vercel.app/?number=")
PINCODE_API = os.getenv("API_PINCODE", "https://pincode-ng.vercel.app/lookup?pincode=")
RC_API = os.getenv("API_VEHICLE", "https://vvvin-ng.vercel.app/lookup?rc=")
IMEI_API = os.getenv("API_IMEI", "https://ng-imei-info.vercel.app/?imei_num=")

# Not available yet (safe empty)
GST_API = os.getenv("API_GST", "")
IFSC_API = os.getenv("API_IFSC", "")


# ===========================
# EXTRA SETTINGS
# ===========================

COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Passport Lookup",
    "Email OSINT",
    "Voter ID Lookup"
]

# Required button text (matches handlers)
BACK = "🔙 Back"
SEARCH = "🔎 Search"
CHECK = "✔️ Check Status"
