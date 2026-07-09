import aiosqlite
from config import DB_PATH
from contextlib import asynccontaxtmanager

@asynccontextmanager
async def get_db():
    db = await aiosqlite.connect(DB_PATH)
    try:
        yield db
    finally:
        await db.close()

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                phone TEXT
            )
        """)
        
        await db.execute("""
            CREATE TABLE IF NOT EXISTS booking(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                date TEXT,
                zone TEXT,
                pack TEXT
            )
        """)

        await db.commit()
