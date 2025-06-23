import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import register_handlers

# .env fayldan token va admin_id ni o‘qish
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN .env fayldan topilmadi!")
        return

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # 🔗 Barcha komandalarni bog‘lash
    register_handlers(application)

    # ♻️ Botni 24/7 ushlab turish
    print("🤖 Resume AI Premium bot ishga tushdi!")
    application.run_polling()

if __name__ == "__main__":
    main()
