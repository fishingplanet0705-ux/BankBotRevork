from .db import DB_NAME
import aiosqlite

def calc_percent(rating):
    if rating <= 3:
        return 25
    elif rating <= 5:
        return 15
    elif rating <= 8:
        return 10
    else:
        return 5

async def create_loan(username, amount, days, percent):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO loans(username, amount, days, percent, status) VALUES(?,?,?,?,?)",
            (username, amount, days, percent, "pending")
        )
        await db.commit()

async def get_loans(status="pending"):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT * FROM loans WHERE status=?",
            (status,)
        ) as cur:
            return await cur.fetchall()

async def approve_loan(loan_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE loans SET status='approved' WHERE id=?",
            (loan_id,)
        )
        await db.commit()

async def deny_loan(loan_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE loans SET status='denied' WHERE id=?",
            (loan_id,)
        )
        await db.commit()
