from telegram import Update
from telegram.ext import ContextTypes
import os

ADMIN_ID = int(os.getenv("ADMIN_ID", "12345678"))

# 🛠 Admin panel menyusini chiqarish
async def show_admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Sizda admin huquqi yo‘q.")
        return

    await update.message.reply_text(
        "🛡 <b>Admin panel</b>\n\n"
        "Buyruqlar:\n"
        "/approve <user_id> – foydalanuvchi to‘lovini tasdiqlash\n"
        "/broadcast <matn> – barcha foydalanuvchilarga xabar yuborish",
        parse_mode="HTML"
    )

# ✅ To‘lovni tasdiqlash
async def approve_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Sizda bu amalni bajarish huquqi yo‘q.")
        return

    if not context.args:
        await update.message.reply_text("⚠️ Foydalanuvchi ID sini yozing: /approve <user_id>")
        return

    tr
