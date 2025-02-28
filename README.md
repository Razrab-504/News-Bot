# Новостной Бот на Aiogram

Этот проект представляет собой новостного бота, созданного с использованием библиотеки Aiogram. Бот позволяет пользователям получать последние новости по различным категориям, используя API новостей.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/bot_aiogram.git
    cd bot_aiogram
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # Для Windows
    # source venv/bin/activate  # Для MacOS/Linux
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

## Настройка

1. Получите API ключ для новостей с [NewsAPI](https://newsapi.org/).

2. Создайте файл `.env` в корне проекта и добавьте ваш API ключ:
    ```env
    NEWS_API_KEY=your_api_key_here
    ```

3. Убедитесь, что ваш бот Telegram настроен и у вас есть токен бота. Добавьте его в файл `.env`:
    ```env
    BOT_TOKEN=your_bot_token_here
    ```

## Запуск

Запустите бота с помощью следующей команды:
```sh
python main.py

