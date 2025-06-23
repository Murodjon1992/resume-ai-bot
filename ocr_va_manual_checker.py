import os
from telegram import Update
from telegram.ext import ContextTypes
from check_ocr import check_payment_from_image
from manual_verifier import send_to_admin_for_review

ADMIN_ID = int(os.getenv("ADMIN_ID", "12345678"))
CARD_LAST4 = "2846"
MIN_AMOUNT = 10000

async def handle_payment_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if not update.message.photo:
        await update.message.reply_text("❗ Iltimos, to‘lov skrinshotini yuboring.")
        return

    # Chek rasmini yuklab olamiz
    photo_file = await update.message.photo[-1].get_file()
    image_path = f"{user.id}_payment.jpg"
    await photo_file.download_to_drive(image_path)

    # OCR orqali avtomatik tekshirish
    is_valid = check_payment_from_image(image_path, expected_card_last4=CARD_LAST4, min_amount=MIN_AMOUNT)

    if is_valid:
        await update.message.reply_text("✅ To‘lov muvaffaqiyatli aniqlandi! Rezyume tayyorlashni boshlaymiz.")
        # Bu yerga rezyume bosqichiga o‘tish kodini qo‘shing
    else:
        await update.message.reply_text("❗ To‘lovni aniqlab bo‘lmadi. Admin tekshiruvi uchun yuborildi.")
        await send_to_admin_for_review(update, context)

    # Foydalanuvchi yuborgan rasmni o‘chirish
    try:
        os.remove(image_path)
    except:
        pass
