import asyncio
from aiogram import Bot, Dispatcher, Router
from handlers import router # Импортируем роутер из handlers.py

# Создаем бота

token = '7661943891:AAHaxVLTnXuTC7IMZzHoFxOIro8OLY3CB1U' # Токен бота
bot = Bot(token)
dp = Dispatcher() # Создаем диспетчер


# Основная функция запуска бота
async def main():
    dp.include_router(router) # Подключаем роутер
    await dp.start_polling(bot)
    
    
# Запускаем бота если файл запущен напрямую
if __name__ == '__main__':
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Бот остановлен')

