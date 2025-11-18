# ===============================
# 📌 CONFIGURATION FILE
# ===============================

# Bot Identity
BOT_USERNAME = "NaGIOsintProBot"        # Without @
BOT_NAME = "Nagi OSINT PRO"

# Bot Token
BOT_TOKEN = "PUT-YOUR-BOT-TOKEN-HERE"

# Channels
MAIN_CHANNEL = "@AbdulBotz"             # Only this is checked in handlers.py
PUBLIC_CHANNEL = "@AbdulBotz"           # For compatibility (same as MAIN)
BACKUP_CHANNEL = "https://t.me/+mPzuc3vtf0c0ZWI9"    # NO CHECK, only informational

# Private Invite Link
PRIVATE_INVITE = "https://t.me/+hyVTTQkfJS41NTFl"

# Referral (optional handlers.py uses it)
REFERRAL_ENABLED = True

# Support Owner
OWNER_USER = "@AbdulBitz"

# ============================
# API ENDPOINTS
# Handlers.py specifically expects:
# MOBILE_API, RC_API, PINCODE_API, IMEI_API, GST_API, IFSC_API
# ============================

MOBILE_API = "https://ph-ng-pi.vercel.app/?number="
RC_API = "https://vvvin-ng.vercel.app/lookup?rc="
PINCODE_API = "https://api.postalpincode.in/pincode/"
IMEI_API = "https://ng-imei-info.vercel.app/?imei_num="
GST_API = "https://your-gst-api.com/?gst="  # update with real API
IFSC_API = "https://your-ifsc-api.com/?ifsc="  # update with real API

# ============================
# Coming Soon Tools
# ============================
COMING_SOON_LIST = [
    "Aadhaar Lookup",
    "PAN Lookup",
    "Voter ID Lookup",
    "Passport Lookup",
    "Email Lookup",
]

# ============================
# UI Fonts / Banner
# ============================

TITLE_FONT = "✦ 𝗡𝗮𝗴𝗶 𝗢𝗦𝗜𝗡𝗧 𝗣𝗥𝗢 ✦"

WELCOME_BANNER = f"""
✨ {TITLE_FONT} ✨

🛡 Multi-Search Intelligence Platform  
⚡ Real-Time Database Lookup Engine  

👇 Choose a Lookup Tool Below
"""
