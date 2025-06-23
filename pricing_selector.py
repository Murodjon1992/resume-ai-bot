from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def show_pricing_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🟢 Oddiy – 10 000 so‘m", callback_data='plan_basic'),
        ],
        [
            InlineKeyboardButton("🟡 O‘rtacha – 20 000 so‘m", callback_data='plan_standard'),
        ],
        [
            InlineKeyboardButton("🔴 Premium – 30 000 so‘m", callback_data='plan_premium'),
        ],
    ]

    await update.message.reply_text(
        "💰 Iltimos, rezyume uchun tarifni tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def handle_pricing_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    selected_plan = query.data

    if selected_plan == "plan_basic":
        amount = 10000
        plan_name = "🟢 Oddiy"
    elif selected_plan == "plan_standard":
        amount = 20000
        plan_name = "🟡 O‘rtacha"
    elif selected_plan == "plan_premium":
        amount = 30000
        plan_name = "🔴 Premium"
    else:
        await query.edit_message_text("❗ Noto‘g‘ri tanlov.")
        return

    # Foydalanuvchining tanlagan tarifini eslab qolamiz
    context.user_data["selected_plan"] = plan_name
    context.user_data["payment_amount"] = amount

    payment_info = (
        f"{plan_name} rezyume uchun to‘lov: {amount} so‘m.\n\n"
        "💳 Karta raqami: <code>5614 6812 2374 2846</code>\n"
        "👤 Karta egasi: <b>URAIMJONOV MURODJON</b>\n\n"
        "✅ To‘lovni amalga oshiring va chekning skrinshotini yuboring.\n"
        "🔍 Bot avtomatik tekshiradi yoki admin ko‘radi."
    )

    await query.edit_message_text(payment_info, parse_mode="HTML")
