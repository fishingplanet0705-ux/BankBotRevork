from aiogram import types
from bot.services.credits import create_loan, calc_percent
from bot.services.users import get_user
from bot.keyboards.inline import credit_menu

async def credit(msg: types.Message):
    args = msg.text.split()

    amount = float(args[1])
    days = int(args[2])

    user = await get_user(msg.from_user.username)
    percent = calc_percent(user[1])

    await msg.answer(
        "Подать заявку?",
        reply_markup=credit_menu(amount, days)
    )
