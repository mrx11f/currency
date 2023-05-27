from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os
import logging
import requests

load_dotenv('.env')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)

inline_buttons1 = [
    InlineKeyboardButton('Конвертировать', callback_data='con_curr'),
]
inline = InlineKeyboardMarkup().add(*inline_buttons1)

inline_buttons2 = [
    InlineKeyboardButton('USD to KGZ', callback_data='usd_kgz'),
    InlineKeyboardButton('EUR to KGZ', callback_data='eur_kgz'),
    InlineKeyboardButton('RUB to KGZ', callback_data='rub_kgz'),
    InlineKeyboardButton('KZT to KGZ', callback_data='kzt_kgz')    
]
inline2 = InlineKeyboardMarkup().add(*inline_buttons2)

@dp.callback_query_handler(lambda call: call)
async def all_inline(call):
    if call.data == 'usd_kgz':
        await usd_kgz(call.message)
    elif call.data == 'eur_kgz':
        await eur_kgz(call.message)
    elif call.data == 'rub_kgz':
        await rub_kgz(call.message)
    elif call.data == 'kzt_kgz':
        await kzt_kgz(call.message)
    elif call.data == 'con_curr':
        await con_curr(call.message)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply(f"Здравствуйте {message.from_user.full_name}. В этом боте вы можете посмотреть текущие курсы разных валют для этого введите команду /currency. ", reply_markup=inline)

# @dp.message_handler(commands=['usd'])
# async def usd_kgz(message: types.Message):
#     url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     currency = soup.find_all('td', class_='exrate')
#     usd_currency = currency[0].text
#     await message.answer(f"Текущий курс доллара: {usd_currency}")
#     await message.answer(f'Введите сумму для конвертации: ')

#==================================================================================================

async def send_converting_message(message: types.Message):
    await message.answer("Введите сумму для конвертации:")

@dp.message_handler(commands=['usd_kgz'])
async def usd_kgz(message: types.Message):
    await send_converting_message(message)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        amount = float(message.text)
        converted_amount = amount * 87,5900

        await message.reply(f"Вы ввели число: {amount}. Результат: {converted_amount}", reply_markup=inline2)
    except ValueError:
        await message.reply("Некорректный формат числа. Введите число с плавающей точкой.")
# =====================================================================================================
# @dp.message_handler(commands=['eur'])
# async def eur_kgz(message: types.Message):
#     url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     currency = soup.find_all('td', class_='exrate')
#     eur_currency = currency[2].text
#     await message.answer(f"Текущий курс евро: {eur_currency}")
    # ==========================================================
async def send_converting_message(message: types.Message):
    await message.answer("Введите сумму для конвертации:")

@dp.message_handler(commands=['usd_kgz'])
async def eur_kgz(message: types.Message):
    await send_converting_message(message)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        amount = float(message.text)
        converted_amount = amount * 93,9228  

        await message.reply(f"Вы ввели число: {amount}. Результат: {converted_amount}", reply_markup=inline2)
    except ValueError:
        await message.reply("Некорректный формат числа. Введите число с плавающей точкой.")
# ==============================================================
# @dp.message_handler(commands=['rub'])
# async def rub_kgz(message: types.Message):
#     url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     currency = soup.find_all('td', class_='exrate')
#     rub_currency = currency[4].text
#     await message.answer(f"Текущий курс рубля: {rub_currency}")
    # =============================================================
async def send_converting_message(message: types.Message):
    await message.answer("Введите сумму для конвертации:")

@dp.message_handler(commands=['usd_kgz'])
async def rub_kgz(message: types.Message):
    await send_converting_message(message)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        amount = float(message.text)
        converted_amount = amount * 1.0913 

        await message.reply(f"Вы ввели число: {amount}. Результат: {converted_amount}", reply_markup=inline2)
    except ValueError:
        await message.reply("Некорректный формат числа. Введите число с плавающей точкой.")
    # =============================================================

# @dp.message_handler(commands=['kzt'])
# async def kzt_kgz(message: types.Message):
#     url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')
#     currency = soup.find_all('td', class_='exrate')
#     kzt_currency = currency[6].text
#     await message.answer(f"Текущий курс тенге: {kzt_currency}")
# ================================================================
async def send_converting_message(message: types.Message):
    await message.answer("Введите сумму для конвертации:")

@dp.message_handler(commands=['usd_kgz'])
async def kzt_kgz(message: types.Message):
    await send_converting_message(message)

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        amount = float(message.text)
        converted_amount = amount * 0.1961  

        await message.reply(f"Вы ввели число: {amount}. Результат: {converted_amount}", reply_markup=inline2)
    except ValueError:
        await message.reply("Некорректный формат числа. Введите число с плавающей точкой.")
# ================================================================

@dp.message_handler(commands=['Конвертировать'])
async def con_curr(message:types.Message):
    await message.answer(f"Выберите валюту для конвертации: ", reply_markup=inline2)

# @dp.message_handler(commands=['usd'])
# async def usd_curr(message:types.Message):
#     await message.reply("Введите сумму для конвертации: ")

@dp.message_handler(commands='currency')
async def get_currency(message: types.Message):
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    currency = soup.find_all('td', class_='exrate')
    usd_currency = currency[0].text
    eur_currency = currency[2].text
    rub_currency = currency[4].text
    kzt_currency = currency[6].text
    await message.answer(f"""Вот текущие данные:
USD: {usd_currency}
EUR: {eur_currency}
RUB: {rub_currency}
KZT: {kzt_currency}""")
    

executor.start_polling(dp, skip_updates=True)
