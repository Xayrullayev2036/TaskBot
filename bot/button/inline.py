from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.button.text import order_accept, accept


def send_data():
    design = [
        [InlineKeyboardButton(order_accept, callback_data=order_accept)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


def check_data():
    design = [
        [InlineKeyboardButton(accept, callback_data=accept)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)

