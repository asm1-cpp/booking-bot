import aiosqlite
from config import DB_PATH
from app.database.db import get_db

class UserRepository:
    @staticmethod
    async def create_user(user_id: int, username: str, phone: str):
        async with get_db() as db:
            await db.execute("INSERT INTO users (user_id, username, phone) VALUES (?, ?, ?)",(user_id, username, phone))

    @staticmethod
    async def get_user(user_id: int):
        async with get_db() as db:
            cursor = await db.execute(
                "SELECT * FROM users WHERE user_id = ?", 
                (user_id, )
            )

            row = await cursor.fetchone()

            return row

class BookingRepository:
    @staticmethod
    async def create_bk_user(user_id: int, date: str, zone: str, pack: str):
        async with get_db() as db:
            await db.execute("INSERT INTO booking (user_id, date, zone, pack) VALUES (?, ?, ?, ?)", (user_id, date, zone, pack))

    @staticmethod
    async def get_bk_user(user_id: int):
        async with get_db() as db:
            cursor = await db.execute(
                "SELECT * FROM booking WHERE user_id = ?",
                (user_id, )
            )

            row = await cursor.fetchone()

            return row
