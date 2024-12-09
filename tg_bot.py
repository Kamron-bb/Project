from aiogram import types, Dispatcher, Bot
from aiogram.filters import Command
import asyncio
from random import randint
import requests

Token="7561703306:AAFBfbDxDlqvv_FR7jya0M4E7EwiPF339do"
bot = Bot(token=Token)
dp = Dispatcher()

user_data = {}
email = "kamolovkamron34@gmail.com"
password = ""
def get_eskiz_token(email,password)
    url = "https://notify.eskiz.uz/api/auth/login"
    payload = {
        'email':email,
        'password':password
    }
    headers = {}
    response = requests.post(url, data=payload,headers=headers)
    if response.status_code ==200:
        return response.json().get('data',{}).get("token")
    if response.json()['data'] is not None:
        pass


@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == '/start':
        await start(message)
    elif 'phone' not in user_data[user_id]:
        await sent_code(message)
    elif 'status' not in user_data[user_id]:
        await check_code(message)
    elif 'location' not in user_data[user_id]:
        await save_address(message)
    elif 'kategoriyalar'   in user_data[user_id]['keyboard']:
        await show_menu(message)
    elif 'tovarlar'  in user_data[user_id]['keyboard']:
        await show_item(message)
    elif 'tanlangan_tovar' in user_data[user_id]['keyboard']:
        await select_item(message)

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text='Share Contact', request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, one_time_keyboard=True, resize_keyboard=True)
    await message.answer(f"Assalomu alaykum! Les Ailes yetkazib berish"
                         f"xizmatiga xush kelibsiz!\n"
                         f"Iltimos telefon raqamingizni kiriting:", reply_markup=keyboard)
    print(user_data)
