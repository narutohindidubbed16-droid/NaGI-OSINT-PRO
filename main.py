# ===============================
# 📌 main.py
# Run Nagi OSINT PRO Bot
# ===============================

import asyncio
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers import (
    start,
    verify_join,
    buttons,
    process_text
)


# ==========================
# BUILD APPLICATION
# ==========================
def main():
    print("🚀 Nagi OSINT PRO Bot Starting…")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # -------- Commands --------
    app.add_handler(CommandHandler("start", start))

    # -------- Callback Buttons --------
    app.add_handler(CallbackQueryHandler(verify_join, pattern="verify_join"))
    app.add_handler(CallbackQueryHandler(buttons))

    # -------- User Text Input (Phone/IMEI/RC/pincode/etc) --------
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))

    print("✅ Bot is now running…")
    app.run_polling()


# ==========================
# EXECUTE BOT
# ==========================
if __name__ == "__main__":
    main()
