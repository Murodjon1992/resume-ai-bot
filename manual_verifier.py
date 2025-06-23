from telegram import Update
from telegram.ext import ContextTypes
import os

ADMIN_ID = int(os.getenv("ADMIN_ID", "12345678"))  # .env fayldan olinadi

async def send_to_admin_for_review(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        photo_path = await photo_file.download_to_drive()
        
        caption = (
            f"📩 Yangi to‘lov tekshiruvi\n"
            f"👤 @{user.username} ({user.id})\n"
            f"Ismi: {user.full_name}\n\n"
            "To‘lov rasm qo‘shilgan. Tekshirib, tasdiqlang."
        )

        with open(photo_path, "rb") as img:
            await context.bot.send_photo(
                chat_id=ADMIN_ID,
                photo=img,
                caption=caption
            )

        await update.message.reply_text("✅ Chek admin tekshiruvi uchun yuborildi.")
    else:
        await update.message.reply_text("❗ Iltimos, to‘lov tasdiq rasmni yuboring.")

async def approve_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Sizda bu amalni bajarish huquqi yo‘q.")
        return

    try:
        args = context.args
        if not args:
            await update.message.reply_text("❗ Foydalanuvchi ID sini yuboring: /approve <user_id>")
            return

        user_id = int(args[0])
        await context.bot.send_message(chat_id=user_id, text="✅ To‘lovingiz admin tomonidan tasdiqlandi. Endi rezyume tayyorlashni davom ettiring.")
        await update.message.reply_text(f"✅ Foydalanuvchi {user_id} ga xabar yuborildi.")
    except Exception as e:
        await update.message.reply_text(f"Xatolik: {e}")
