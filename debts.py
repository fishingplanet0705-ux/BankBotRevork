from .db import DB
import aiosqlite

async def add_debt(user_id, username, amount):
    async with aiosqlite.connect(DB) as db:
        await db.execute(
            "INSERT INTO debts VALUES(?,?,?)",
            (user_id, username, amount)
        )
        await db.commit()

async def get_debts():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM debts") as cur:
            return await cur.fetchall()
