from aiogram.utils.keyboard import InlineKeyboardBuilder
from content import BUTTONS1

def hello_kb():
    builder = InlineKeyboardBuilder()

    for callback_data, text in BUTTONS1.items():
        builder.button(text=text, callback_data=callback_data)

    builder.adjust(2,2)

    return builder.as_markup()

def back_kb():
    builder = InlineKeyboardBuilder()

    builder.button(text="Назад в меню", callback_data="back_to_menu")

    return builder.as_markup()
