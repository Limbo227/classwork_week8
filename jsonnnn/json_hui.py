import requests
from aiogram import Bot, types
from aiogram.dispatcher import dispatcher
from aiogram.utils import executor
from pprint import pprint as pp
from aiogram.dispatcher import Dispatcher

openweather = '5febe2f987942d81ac43be0ca14853a8'
tg_bot_token  = '5096086105:AAFqo-WKhM5IsAWbrhg65L2eo85-Pvym-1U'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Салам бро, да будет погода")

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(f'''https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={openweather}&units=metric&lang=ru''')
        data = r.json()
        city = data['name']
        weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        feels_like = data['main']['feels_like']


        await message.reply(f"""
    City - {city},
    Temparature - {weather},
    Humidity - {humidity},
    Pressure - {pressure},
    feels_like - {feels_like}    
    """)
    except:
        print("Error")

if __name__ == '__main__':
    executor.start_polling(dp)





