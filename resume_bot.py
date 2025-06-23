from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)
from questionnaire import ask_next_question, handle_user_answer
from pricing_selector import pricing_menu_handler
from language_manager import set_language
from oferta_uz import show_offer_text
from resume_builder_pdfkit import generate_resume_pdf

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    context.user_data.clear()

    language_keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("🇺🇿 O‘zbekcha"), KeyboardButton("🇷🇺 Русский")],
            [KeyboardButton("🇬🇧 English")]
        ],
        resize_keyboard=True
    )

    await update.message.reply_text(
        f"Assalomu alaykum, {user.first_name}!\n\n"
        "Tilni tanlang / Choose your language:",
        reply_markup=language_keyboard
    )

# Har qanday matnli xabarga ishlovchi
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_lang = context.user_data.get("lang")

    if text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English"]:
        await set_language(update, context, text)
        await ask_next_question(update, context)
    elif user_lang:
        await handle_user_answer(update, context)
    else:
        await update.message.reply_text("Iltimos, dastlab tilni tanlang!")

def start_bot(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    application.add_handler(CallbackQueryHandler(pricing_menu_handler))
