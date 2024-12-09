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
