import aiosqlite

DB_NAME = "bank.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            username TEXT PRIMARY KEY,
            rating REAL DEFAULT 5.0,
            credits_taken INTEGER DEFAULT 0,
            total_credit REAL DEFAULT 0
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS admins(
            username TEXT PRIMARY KEY
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS loans(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            amount REAL,
            days INTEGER,
            percent REAL,
            status TEXT
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            admin TEXT,
            target TEXT
        )
        """)

        await db.commit()
