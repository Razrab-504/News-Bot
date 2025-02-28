from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import keyboard as kb
from keyboard import get_news  # Импортируем функцию get_news

router = Router() # Создаем роутер

@router.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer('Привет! Я новостной бот! Напиши /news чтобы получить новости') # Приветствие

@router.message(Command('news'))
async def get_news_cmd(message: Message):
    await message.answer("Выберите категорию новостей", reply_markup=await kb.category_markup()) # Выбор категории новостей с кнопками

# Обработка нажатий на кнопки Категорий
@router.callback_query(F.data.startswith('callback_'))
async def callback_category(query: CallbackQuery):
    category = query.data.split('_')[1]  # Получаем категорию из callback_data
    news_dict = await get_news(category)  # Получаем новости по категории
    if news_dict:
        news_message = '\n\n'.join([f"{title}\n{url}" for title, url in news_dict.items()])
        await query.message.answer(news_message)  # Отправляем новости пользователю
    else:
        await query.message.answer('Не удалось получить новости. Попробуйте позже.')

@router.callback_query(F.data == 'start')
async def start_callback(query: CallbackQuery):
    await query.message.answer('Вы вернулись в начало! Напиши /news чтобы получить новости') # Возвращаемся в начало

