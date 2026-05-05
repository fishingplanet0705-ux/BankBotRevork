from aiogram import types
from bot.services.credits import get_pending_loans, approve_loan, deny_loan
from bot.services.admins import add_admin
from bot.keyboards.inline import loan_kb
from bot.services.db import DB
import aiosqlite

# ➕ добавить админа
async def addadmin(msg: types.Message):
    if msg.reply_to_message:
        u = msg.reply_to_message.from_user
        await add_admin(u.id, u.username)
        await msg.answer("✅ Админ добавлен")

# 📋 панель
async def admin_panel(msg: types.Message):
    loans = await get_pending_loans()

    if not loans:
        return await msg.answer("Нет заявок")

    for loan in loans:
        await msg.answer(
            f"📢 Заявка #{loan[0]}\n"
            f"👤 @{loan[2]}\n"
            f"💰 {loan[3]}\n"
            f"📅 {loan[4]} дней\n"
            f"📊 {loan[5]}%",
            reply_markup=loan_kb(loan[0])
        )

# ✅ одобрение
async def approve(callback: types.CallbackQuery):
    loan_id = int(callback.data.split("_")[1])

    await approve_loan(loan_id)

    async with aiosqlite.connect(DB) as db:
        async with db.execute(
            "SELECT user_id FROM loans WHERE id=?",
            (loan_id,)
        ) as cur:
            user_id = (await cur.fetchone())[0]

    await callback.bot.send_message(
        user_id,
        "✅ Ваш кредит одобрен"
    )

# ❌ отказ
async def deny(callback: types.CallbackQuery):
    loan_id = int(callback.data.split("_")[1])

    await deny_loan(loan_id)

    async with aiosqlite.connect(DB) as db:
        async with db.execute(
            "SELECT user_id FROM loans WHERE id=?",
            (loan_id,)
        ) as cur:
            user_id = (await cur.fetchone())[0]

    await callback.bot.send_message(
        user_id,
        "❌ Ваш кредит отклонён, свяжитесь с банком @ArabovBa"
    )
