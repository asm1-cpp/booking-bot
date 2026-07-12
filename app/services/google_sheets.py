from google.oauth2.service_account import Credentials
import asyncio
import gspread_asyncio
from config import SPREADSHEET_ID


def get_creds():
    creds = Credentials.from_service_account_file("credentials.json")
    scoped = creds.with_scopes([
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped

agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)

async def append_booking(user_id, username, zone, pack, date_time):
    cl = await agcm.authorize()
    spsh = await cl.open_by_key(SPREADSHEET_ID)
    
    worksheet = await spsh.worksheet("Записи")

    row_data = [user_id, username, zone, pack, date_time]

    await worksheet.append_row(row_data)

async def append_users(user_id, username):
    cl = await agcm.authorize()
    spsh = await cl.open_by_key(SPREADSHEET_ID)

    worksheet = await spsh.worksheet("Пользователи")

    row_data = [user_id, username]

    await worksheet.append_row(row_data)
