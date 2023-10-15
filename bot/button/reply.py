from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.button.text import buyurtma_berish, phone, location, new_order


def order_button():
    design = [
        [buyurtma_berish]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def new_order_button():
    design = [
        [new_order]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def phone_number_button():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton("Telefon raqamni yuborish", request_contact=True)]],
                               resize_keyboard=True, one_time_keyboard=True)


def location_button():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton("Joylashuvni yuborish", request_location=True)]],
                               resize_keyboard=True, one_time_keyboard=True)
