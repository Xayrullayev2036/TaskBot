from bot.button.reply import order_button
from bot.dispatcher import dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands="start")
async def start_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f"Assalomu aleykum {msg.from_user.full_name} botimizga xush kelibsiz")
    await msg.answer("Buyurtma berishni boshlaymizmi😉", reply_markup=order_button())
    await state.set_state("get_data")


@dp.message_handler(state="refresh")
async def start_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Buyurtma berishni boshlaymizmi😉", reply_markup=order_button())
    await state.set_state("get_data")
