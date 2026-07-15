from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters.command import Command

from app.keyboards.start_menu_keyboard import hello_kb
from app.utils.content import HELLO_MESSAGE as hello_msg

my_router = Router(name="router")

@router.message(Command("start"))
async def start_message(message: Message):
    await message.answer(hello_msg, reply_markup = hello_kb())
