from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from admin_panel import show_admin_panel, approve_user, broadcast_message
from questionnaire import ask_next_question, handle_user_answer
from pricing_selector import show_pricing_options, handle_pricing_selection
from ocr_va_manual_checker import handle_payment_image

def register_handlers(application: Application):
    # ➕ Foydalanuvchi boshlanishi
    application.add_handler(CommandHandler("start", show_pricing_options))

    # 📄 Narx tanlovi
    application.add_handler(CallbackQueryHandler(handle_pricing_selection, pattern="^plan_"))

    # 🧾 To‘lov tasdiqlash uchun chek yuborish
    application.add_handler(MessageHandler(filters.PHOTO, handle_payment_image))

    # 📋 Savollar va javoblar
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_user_answer))

    # 🛡 Admin buyruqlari
    application.add_handler(CommandHandler("admin", show_admin_panel))
    application.add_handler(CommandHandler("approve", approve_user))
    application.add_handler(CommandHandler("broadcast", broadcast_message))
