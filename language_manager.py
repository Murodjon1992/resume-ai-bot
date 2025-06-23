from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

LANGUAGE_KEYBOARD = ReplyKeyboardMarkup(
    [["🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English"]],
    resize_keyboard=True
)

async def ask_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Iltimos, tilni tanlang:\n\nPlease select a language:\n\nПожалуйста, выберите язык:",
        reply_markup=LANGUAGE_KEYBOARD
    )

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.message.text
    if lang == "🇺🇿 O‘zbekcha":
        context.user_data["language"] = "uz"
    elif lang == "🇷🇺 Русский":
        context.user_data["language"] = "ru"
    elif lang == "🇬🇧 English":
        context.user_data["language"] = "en"
    else:
        await update.message.reply_text("❗ Tanlangan til tushunarsiz.")
        return

    await update.message.reply_text("✅ Til tanlandi. Bot ishga tayyor!")
