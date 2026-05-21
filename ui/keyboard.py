from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="username scan")],
            [KeyboardButton(text="phone scan")],
            [KeyboardButton(text="email scan")],
            [KeyboardButton(text="domain scan")]
        ],
        resize_keyboard=True
    )
