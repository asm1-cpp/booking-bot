from aiogram.utils.keyboard import InlineKeyboardBuilder
from content import BUTTONS1

def get_hello_menu_keyboard():
    builder = InlineKeyboardBuilder()

    for callback_data, text in BUTTONS1.items():
        builder.button(text=text, callback_data=callback_data)

    builder.adjust(2,2)

    return builder.as_markup()
