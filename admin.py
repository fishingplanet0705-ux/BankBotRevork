from aiogram import types
from bot.services.credits import get_loans, approve_loan, deny_loan
from bot.keyboards.inline import admin_loan_kb

async def admin_panel(msg: types.Message):
    loans = await get_loans()

    for loan in loans:
        await msg.answer(
            f"Заявка #{loan[0]}\n@{loan[1]}\n{loan[2]}₽",
            reply_markup=admin_loan_kb(loan[0])
        )
