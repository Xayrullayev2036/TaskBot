# # # User start bossa — Buyurtma berish tugmasi chiqishi kerak
# # #
# # # Buyurtma berishni bossa — uje statelar orqali Userdan quyidagi ma'lumotlarni olishi kerak
# # #      1. name
# # #      2. recept == rasm, file, text hohlaganini kiritishi kerak
# # #      3. phone
# # #      4. location
# # #
# # # bularni hammasini bot inline tugma bilan guruhga yuborsa guruhdagi delivery workerlar tugmani bosib buyurtmani olsa #active turgani #olindi bo'lib qolishi kerak
# # #
# # # dB - SQLite3
# # from bot.dispatcher import bot
# #
# #
# # # from aiogram import Bot
# # #
# # # # Botni yaratish
# # # bot = Bot(token='6401583362:AAEgppyKN9v-cRgvQQF5vlOOfV51H8INKP8')
# # #
# # #
# # # async def get_chat_id():
# # #     print("start")
# # #     bot = Bot(token='6401583362:AAEgppyKN9v-cRgvQQF5vlOOfV51H8INKP8')
# # #     messages = await bot.get_my_commands()
# # #     message = messages[-1]  # Eng oxirgi xabar (forward qilingan xabar)
# # #     print("continue")
# # #     chat_id = message.forward_from_chat.id  # forward qilingan guruhning chat_id sini olish
# # #     print(chat_id)
# # #
# # # https://api.telegram.org/fast_foods_order_bot:6401583362:AAEgppyKN9v-cRgvQQF5vlOOfV51H8INKP8/getUpdates
# #
# #
# #
# # async def data_send_group(data):
# #     result = data
# #     await bot.send_message(chat_id=-1001949758516, text=data)
#
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.types import ChatType
# from aiogram.utils import executor
#
# API_TOKEN = '6401583362:AAEgppyKN9v-cRgvQQF5vlOOfV51H8INKP8'
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# async def send_group_message(chat_id):
#
# @dp.message_handler(commands='send_message_to_group')
# async def send_message_to_group(message: types.Message):
#     # Foydalanuvchi guruhdagi adminmi?
#     if message.chat.type == ChatType.GROUP:
#         await send_group_message(message.chat.id)
#
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)
