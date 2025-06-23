from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from resume_builder_pdfkit import generate_resume_pdf

questions = [
    "👤 To‘liq ismingizni kiriting:",
    "🎓 Ma’lumotingiz:",
    "📞 Telefon raqamingiz:",
    "📍 Yashash manzilingiz:",
    "💼 Ish tajribangiz (kompaniya nomi, lavozim, davri):",
    "🛠 Qaysi ko‘nikmalarga egasiz?",
    "🌐 Qaysi tillarni bilasiz?",
    "📌 Qo‘shimcha ma’lumotlaringiz (agar bo‘lsa):",
]

question_keys = [
    "full_name", "education", "phone", "address",
    "experience", "skills", "languages", "extra",
]

async def ask_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_index = context.user_data.get("question_index", 0)

    if current_index < len(questions):
        await update.message.reply_text(questions[current_index])
        context.user_data["question_index"] = current_index + 1
    else:
        await generate_and_send_resume(update, context)

async def handle_user_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_index = context.user_data.get("question_index", 1)
    key = question_keys[current_index - 1]
    context.user_data[key] = update.message.text

    await ask_next_question(update, context)

async def generate_and_send_resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("♻️ Rezyumeni yaratmoqdaman...")

    file_path = generate_resume_pdf(context.user_data)

    with open(file_path, "rb") as f:
        await update.message.reply_document(f, caption="✅ Rezyume tayyor!")
