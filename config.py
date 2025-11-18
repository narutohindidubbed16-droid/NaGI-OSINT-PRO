# ===========================
# ⚙️ CONFIGURATION FILE
# ===========================

import os

# ============= BASIC BOT SETTINGS =============
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NaGIOsintProBot")

MAIN_CHANNEL = os.getenv("MAIN_CHANNEL", "@AbdulBitz")
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "@dummybackup")  # Just placeholder, check disabled

START_CREDITS = 10   # same as handlers.py expects

# ============= API LINKS =============

# Your working APIs
MOBILE_API = os.getenv("API_MOBILE", "https://ph-ng-pi.vercel.app/?number=")
PINCODE_API = os.getenv("API_PINCODE", "https://pincode-ng.vercel.app/lookup?pincode=")
RC_API = os.getenv("API_VEHICLE", "https://vvvin-ng.vercel.app/lookup?rc=")
IMEI_API = os.getenv("API_IMEI", "https://ng-imei-info.vercel.app/?imei_num=")

# Not available (avoid errors by adding empty)
GST_API = ""
IFSC_API = ""

# ============= OTHER SETTINGS =============
PRIVATE_INVITE = os.getenv("PRIVATE_INVITE", "")
OWNER_USER = os.getenv("OWNER_USER", "@AbdulBitz")
