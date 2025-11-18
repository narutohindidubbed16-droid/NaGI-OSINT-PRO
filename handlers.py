# ===============================
# 📌 handlers.py
# All Bot Logic & API Processors
# ===============================

import aiohttp
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes
from config import (
    BOT_USERNAME,
    MAIN_CHANNEL,
    BACKUP_CHANNEL,
    START_CREDITS,
    MOBILE_API,
    RC_API,
    PINCODE_API,
    IMEI_API,
    GST_API,
    IFSC_API
)
from keyboards import (
    join_channels_kb,
    main_menu_kb,
    ask_input_kb,
    coming_soon_kb
)
from database import (
    create_user,
    get_user_credits,
    decrease_credit,
    add_referral
)


# ==========================
# VERIFY CHANNEL JOIN
# ==========================
async def is_joined(user_id, bot):
    try:
        m1 = await bot.get_chat_member(MAIN_CHANNEL, user_id)
        m2 = await bot.get_chat_member(BACKUP_CHANNEL, user_id)
        return m1.status in ("member", "administrator", "creator") and m2.status in ("member", "administrator", "creator")
    except:
        return False


# ==========================
# START COMMAND
# ==========================
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # Referral check
    args = ctx.args
    if args and args[0].isdigit():
        ref_id = int(args[0])
    else:
        ref_id = None

    created = create_user(user.id, user.username, user.first_name)

    if created and ref_id and ref_id != user.id:
        add_referral(ref_id, user.id)
        try:
            await ctx.bot.send_message(
                chat_id=ref_id,
                text=f"🎉 *New Referral!* Someone joined using your link!\n\nYou earned **+1 Credit** 💳",
                parse_mode="Markdown"
            )
        except:
            pass

    # Channel Check
    if not await is_joined(user.id, ctx.bot):
        await update.message.reply_text(
            "🔐 *Join both channels to unlock Nagi OSINT PRO:*",
            reply_markup=join_channels_kb(),
            parse_mode="Markdown"
        )
        return

    await update.message.reply_text(
        f"👋 Welcome to **Nagi OSINT PRO**\nChoose any tool below ⬇️",
        reply_markup=main_menu_kb(),
        parse_mode="Markdown"
    )


# ==========================
# VERIFY JOIN BUTTON
# ==========================
async def verify_join(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    user_id = q.from_user.id

    if await is_joined(user_id, ctx.bot):
        await q.message.reply_text(
            "✅ *Verification Successful!* You now have full access.",
            reply_markup=main_menu_kb(),
            parse_mode="Markdown"
        )
    else:
        await q.message.reply_text(
            "❌ You still haven't joined both channels!",
            reply_markup=join_channels_kb()
        )


# ==========================
# ASK INPUT HANDLER
# ==========================
async def ask_input(update: Update, ctx: ContextTypes.DEFAULT_TYPE, text):
    await update.callback_query.message.reply_text(
        text,
        reply_markup=ask_input_kb(),
        parse_mode="Markdown"
    )


# ==========================
# CALLBACK HANDLER
# ==========================
async def buttons(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    data = q.data
    await q.answer()

    if data == "mobile_lookup":
        ctx.user_data["mode"] = "mobile"
        await ask_input(update, ctx, "📱 *Send Mobile Number* (ONLY digits):")

    elif data == "rc_lookup":
        ctx.user_data["mode"] = "rc"
        await ask_input(update, ctx, "🚗 *Send RC Number:*")

    elif data == "pincode_lookup":
        ctx.user_data["mode"] = "pincode"
        await ask_input(update, ctx, "📦 *Send Pincode:*")

    elif data == "imei_lookup":
        ctx.user_data["mode"] = "imei"
        await ask_input(update, ctx, "🧾 *Send IMEI Number:*")

    elif data == "gst_lookup":
        ctx.user_data["mode"] = "gst"
        await ask_input(update, ctx, "🏢 *Send GST Number:*")

    elif data == "ifsc_lookup":
        ctx.user_data["mode"] = "ifsc"
        await ask_input(update, ctx, "🏦 *Send IFSC Code:*")

    elif data == "refer":
        uid = q.from_user.id
        ref = f"https://t.me/{BOT_USERNAME}?start={uid}"
        await q.message.reply_text(
            f"🎁 *Refer & Earn*\nShare your unique link:\n\n`{ref}`\n\nEvery signup = **+1 credit** 💳",
            parse_mode="Markdown"
        )

    elif data == "coming_soon":
        await q.message.reply_text(
            "🚧 *Upcoming Mega Tools*",
            reply_markup=coming_soon_kb(),
            parse_mode="Markdown"
        )

    elif data == "back_home":
        await q.message.reply_text(
            "🏠 *Main Menu:*",
            reply_markup=main_menu_kb(),
            parse_mode="Markdown"
        )


# ==========================
# PROCESS USER MESSAGE
# ==========================
async def process_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not await is_joined(user.id, ctx.bot):
        await update.message.reply_text(
            "🔐 Please join required channels first.",
            reply_markup=join_channels_kb()
        )
        return

    # No mode selected
    if "mode" not in ctx.user_data:
        return

    mode = ctx.user_data["mode"]
    data = update.message.text.strip()

    # Credit check
    credits = get_user_credits(user.id)
    if credits <= 0:
        await update.message.reply_text("❌ *No Credits Left!* Use /start → Refer & Earn", parse_mode="Markdown")
        return

    # Deduct credit
    decrease_credit(user.id)

    await update.message.reply_text("⏳ *Fetching Data…*", parse_mode="Markdown")

    # API mapping
    apis = {
        "mobile": MOBILE_API + data,
        "rc": RC_API + data,
        "pincode": PINCODE_API + data,
        "imei": IMEI_API + data,
        "gst": GST_API + data,
        "ifsc": IFSC_API + data
    }

    url = apis.get(mode)

    # API CALL
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as r:
                js = await r.json()
        except:
            await update.message.reply_text("⚠️ API Error. Try again later.")
            return

    # Format output (clean clean)
    txt = f"📄 *Nagi OSINT PRO Result*\n\n```{js}```\n\n🕒 {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"

    await update.message.reply_text(txt, parse_mode="Markdown")
