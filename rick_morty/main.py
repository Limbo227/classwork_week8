import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint as pp

tg_bot_token  = '5096086105:AAFqo-WKhM5IsAWbrhg65L2eo85-Pvym-1U'
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

info = requests.get('https://rickandmortyapi.com/api/character')
data = info.json()
characters = data['results']

new_characters = dict()

for values in characters:
    new_characters[values['name']] = values


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Имя персонажа! ")

@dp.message_handler()
async def get_info_about_character(message: types.Message):
    character = new_characters.get(message.text)
    if character is None:
        await message.reply("sorry not find")
    await  message.reply(f"""
    
    id : {character['id']}
    name : {character['name']}
    status  : {character['status']}
    species : {character['species']}
    type : {character['type']}
    gender : {character['gender']}
    origin : {character['origin']['name']}
    url_origin : {character['origin']['url']}
    location  : {character['location']['name']}
    url_location : {character['location']['url']}
    image = {character['image']}
        
    """)

executor.start_polling(dp)


