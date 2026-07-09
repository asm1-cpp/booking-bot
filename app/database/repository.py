import aiosqlite
from config import DB_PATH

class UserRepository:
    @staticmethod
    async def create_user(user_id: int, username: str, phone: str):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("INSERT INTO users (user_id, username, phone) VALUES (?, ?, ?)",(user_id, username, phone))

            await db.commit()

    @staticmethod
    async def get_user(user_id: int):
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "SELECT * FROM users WHERE user_id = ?", 
                (user_id, )
            )

            row = await cursor.fetchone()

            return row

class BookingRepository:
    @staticmethod
    async def create_booking_user(user_id: int, date: str, zone: str, pack: str):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("INSERT INTO booking (user_id, date, zone, pack) VALUES (?, ?, ?, ?)", (user_id, date, zone, pack))

            await db.commit()

    @staticmethod
    async def get_booking_user(user_id: int):
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "SELECT * FROM booking WHERE user_id = ?",
                (user_id, )
            )

            row = await cursor.fetchone()

            return row
