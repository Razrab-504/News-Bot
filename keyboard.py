from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import requests

name = None

# Функция для получения новостей
async def get_news(category):
    API_KEY = "Your API" # API ключ для новостей
    URL = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}"  # URL для запроса на новости
    response = requests.get(URL)  # requests запрос на новости

    if response.status_code == 200:
        data = response.json()  # Получаем json ответ
        articles = data.get('articles', [])
        
        news_dict = {article['title']: article['url'] for article in articles[:5]}   # Создаем словарь с 5 новостями
        
        return news_dict
    else:
        return None

# Функция для создания клавиатуры с категориями новостей
categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]

async def category_markup():
    keyboard = InlineKeyboardBuilder()
    for category in categories:
        keyboard.add(InlineKeyboardButton(text=category.capitalize(), callback_data=f"callback_{category}"))
    return keyboard.adjust(2).as_markup()

