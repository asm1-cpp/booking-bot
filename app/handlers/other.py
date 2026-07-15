from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from app.utils.content import ABOUT, CONTACTS, SERVICES, HELLO_MESSAGE
from app.keyboards.start_menu_keyboard import back_kb

other_rt = Router(name = "other_rt")

@other_rt.callback_query(F.data = "about")
async def about_company(callback: CallbackQuery):
    await bot.edit_message_text(
        chat_id = calback.message.chat.id,
        message_id = callback.message.message_id,
        text = ABOUT,
        reply_markup = back_kb()
    )
    await callback.answer()

@other_rt.callback_query(F.data = "contact")
async def company_contats(callback: CallbackQuery):
    await bot.edit_message_text(
        chat_id = calback.message.chat.id,
        message_id = callback.message.message_id,
        text = CONTACTS,
        reply_markup = back_kb()
    )
    await callback.answer()

@other_rt.callback_query(F.data = "services")
async def company_services(callback: CallbackQuery):
    await bot.edit_message_text(
        chat_id = calback.message.chat.id,
        message_id = callback.message.message_id,
        text = SERVICES,
        reply_markup = back_kb()
    )
    await callback.answer() 

@other_rt.callback_query(F.data = "back_to_menu")
async def back_to_menu(callback: CallbackQuery):
    await bot.edit_message_text(
        chat_id = calback.message.chat.id,
        message_id = callback.message.message_id,
        text = HELLO_MESSAGE,
        reply_markup = back_kb()
    )
    await callback.answer()
