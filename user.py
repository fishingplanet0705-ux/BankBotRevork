from aiogram import types
from bot.services.users import create_user, get_user, get_top

async def start(msg: types.Message):
    await create_user(msg.from_user.username)
    await msg.answer("✅ Регистрация успешна")

async def profile(msg: types.Message):
    user = await get_user(msg.from_user.username)

    await msg.answer(
        f"👤 @{user[0]}\n⭐ {user[1]}\n💰 {user[2]}"
    )

async def top(msg: types.Message):
    users = await get_top()
    text = "🏆 ТОП:\n"

    for i, u in enumerate(users, 1):
        text += f"{i}. @{u[0]} — {u[1]}\n"

    await msg.answer(text)
