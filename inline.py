from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def credit_menu(amount, days):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Подать заявку", callback_data=f"apply_{amount}_{days}"),
        InlineKeyboardButton("Отмена", callback_data="cancel")
    )
    return kb

def admin_loan_kb(loan_id):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("✅ Одобрить", callback_data=f"approve_{loan_id}"),
        InlineKeyboardButton("❌ Отказать", callback_data=f"deny_{loan_id}")
    )
    return kb
