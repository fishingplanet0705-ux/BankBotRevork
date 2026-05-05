from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def loan_kb(loan_id):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("✅ Одобрить", callback_data=f"approve_{loan_id}"),
        InlineKeyboardButton("❌ Отказать", callback_data=f"deny_{loan_id}")
    )
    return kb
