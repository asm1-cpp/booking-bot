from aiogram.utils.keyboard import InlineKeyboardBuilder
from content import BUTTONS2, BUTTONS3

def zone_kb():
    builder = InlineKeyboardBuilder()

    for callback_data, text in BUTTONS2.items():
        builder.button(text=text, callback_data=callback_data)

    builder.adjust(2,2)

    return builder.as_markup()

def pack_kb():
    builder = InlineKeyboardBuilder()

    for callback_data, text in BUTTONS3.items():
        builder.button(text=text, callback_data=callback_data)

    builder.adjust(2,2)

    return builder.as_markup()
