from .db import DB_NAME
import aiosqlite

async def create_user(username):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users(username) VALUES(?)",
            (username,)
        )
        await db.commit()

async def get_user(username):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ) as cur:
            return await cur.fetchone()

async def update_rating(username, rating):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE users SET rating=? WHERE username=?",
            (rating, username)
        )
        await db.commit()

async def get_top():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT username, rating FROM users ORDER BY rating DESC LIMIT 10"
        ) as cur:
            return await cur.fetchall()
