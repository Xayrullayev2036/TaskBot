import os
import sqlite3

from aiogram.types import ChatType

from bot.button.inline import send_data, check_data
from bot.button.reply import phone_number_button, location_button, order_button, new_order_button
from bot.button.text import name, recept, phone, location, order_accept, buyurtma_berish
from bot.db.config import save_database
from bot.dispatcher import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext, filters
from dotenv import load_dotenv

load_dotenv()
result = None


@dp.message_handler(state="get_data")
async def from_user_get_data(msg: types.Message, state: FSMContext):
    if msg.text == buyurtma_berish:
        await msg.answer(name)
        await state.set_state("get_name")


@dp.message_handler(state="get_name")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        await msg.answer("Raqam kirita olmaysiz.Qayta kiriting")
        await state.get_state("get_data")

    else:
        async with state.proxy() as file:
            file["name"] = msg.text
            file["user_id"] = msg.from_user.id
        await state.set_state("get_recept")
        await msg.answer(recept)


# ======================================RECEPT DATA===========================

@dp.message_handler(content_types=types.ContentType.DOCUMENT, state="get_recept")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    file_id = msg.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{os.getenv('Token')}/{file_path}"
    async with state.proxy() as file:
        file["data"] = file_url
        print(file_url)
    await state.set_state("get_phone")
    await msg.answer(phone, reply_markup=phone_number_button())


@dp.message_handler(content_types=types.ContentType.PHOTO, state="get_recept")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    photo = msg.photo[-1]
    file_id = photo.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    file_url = f"https://api.telegram.org/file/bot{os.getenv('Token')}/{file_path}"

    async with state.proxy() as file:
        file["data"] = file_url
    await state.set_state("get_phone")
    await msg.answer(phone, reply_markup=phone_number_button())


@dp.message_handler(state="get_recept")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    if msg.text.isdigit():
        await msg.answer("Iltimos string malumot kiriting")
    async with state.proxy() as file:
        file["data"] = msg.text
    await state.set_state("get_phone")
    await msg.answer(phone, reply_markup=phone_number_button())


# =====================================END RECEPT DATA====================


@dp.message_handler(content_types=types.ContentType.CONTACT, state="get_phone")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    async with state.proxy() as file:
        file["phone"] = msg.contact.phone_number
    await state.set_state("get_location")
    await msg.answer(location, reply_markup=location_button())


@dp.message_handler(content_types=types.ContentType.LOCATION, state="get_location")
async def from_user_get_name(msg: types.Message, state: FSMContext):
    chat_id = -1001949758516
    async with state.proxy() as file:
        file["latitude"] = msg.location.latitude
        file["longitude"] = msg.location.longitude
        file["status"] = "active"
    message = f"""
Ismi: {file["name"]}
Qo`shimcha ma`lumot: {file["data"]}
Telefon raqami: {file["phone"]}
Joylashuvi:Latitude: {file["latitude"]}Longitude: {file["longitude"]}
"""
    await bot.send_message(chat_id, message, reply_markup=send_data())
    save_database(file)
    await msg.answer("Barcha malumotlar muvaffaqiyatli saqlandi botimizdan foydalanganingiz uchun tashakkur!!!😊",reply_markup=new_order_button())
    await state.set_state("refresh")


@dp.callback_query_handler(lambda c: c.data == order_accept)
async def process_group_inline_button(callback_query: types.CallbackQuery):
    print("hello")
    message_id = callback_query.message.message_id
    chat_id = -1001949758516
    print(callback_query.data)

    if callback_query.data == order_accept:
        print("tcfvgbhnjmk")
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=check_data())



