import aiosqlite

DB = "bank.db"

async def init_db():
    async with aiosqlite.connect(DB) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER,
            username TEXT,
            rating REAL DEFAULT 5.0,
            credits_taken INTEGER DEFAULT 0,
            total_credit REAL DEFAULT 0
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS admins(
            user_id INTEGER,
            username TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS loans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            amount REAL,
            days INTEGER,
            percent REAL,
            status TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS debts(
            user_id INTEGER,
            username TEXT,
            amount REAL
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            action TEXT,
            admin TEXT,
            target TEXT
        )
        """)

        await db.commit()
