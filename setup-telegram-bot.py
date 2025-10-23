#!/usr/bin/env python3
"""
Скрипт для настройки Telegram бота с Mini App
"""

import requests
import json
import sys

# Конфигурация
BOT_TOKEN = "8206490529:AAEeqvt_x8-Ybpi2QhPW442kg68XVc6V2xE"
WEB_APP_URL = "https://your-app-url.vercel.app"  # Замените на ваш URL после деплоя

def setup_bot():
    """Настройка Telegram бота"""
    
    print("🤖 Настройка Telegram бота...")
    
    # 1. Получаем информацию о боте
    bot_info_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
    response = requests.get(bot_info_url)
    
    if response.status_code != 200:
        print("❌ Ошибка получения информации о боте")
        print(f"Ответ: {response.text}")
        return False
    
    bot_info = response.json()
    if not bot_info.get('ok'):
        print("❌ Неверный токен бота")
        return False
    
    bot_data = bot_info['result']
    print(f"✅ Бот найден: @{bot_data['username']} ({bot_data['first_name']})")
    
    # 2. Устанавливаем команды бота
    commands = [
        {"command": "start", "description": "🚀 Запустить приложение"},
        {"command": "help", "description": "❓ Помощь"},
        {"command": "shop", "description": "🛍️ Мой магазин"},
        {"command": "orders", "description": "📦 Мои заказы"},
        {"command": "profile", "description": "👤 Профиль"}
    ]
    
    set_commands_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setMyCommands"
    commands_response = requests.post(set_commands_url, json={"commands": commands})
    
    if commands_response.status_code == 200:
        print("✅ Команды бота установлены")
    else:
        print("⚠️ Не удалось установить команды бота")
    
    # 3. Создаем кнопку с Mini App
    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🛍️ Открыть Marketplace",
                    "web_app": {"url": WEB_APP_URL}
                }
            ],
            [
                {"text": "❓ Помощь", "callback_data": "help"},
                {"text": "👤 Профиль", "callback_data": "profile"}
            ]
        ]
    }
    
    # 4. Устанавливаем описание бота
    description = f"""
🛍️ Telegram Marketplace для блогеров

Продавайте товары и цифровые активы прямо в Telegram!

✨ Возможности:
• Создание собственного магазина
• Продажа физических и цифровых товаров
• Прием заказов и платежей
• Аналитика продаж
• Система отзывов

Нажмите кнопку ниже, чтобы открыть приложение:
    """
    
    set_description_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setMyDescription"
    desc_response = requests.post(set_description_url, json={"description": description})
    
    if desc_response.status_code == 200:
        print("✅ Описание бота установлено")
    else:
        print("⚠️ Не удалось установить описание бота")
    
    # 5. Создаем пример сообщения с кнопкой
    print("\n📝 Пример сообщения для отправки пользователям:")
    print("=" * 50)
    print(f"""
Добро пожаловать в Telegram Marketplace! 🛍️

Здесь вы можете:
• Создать свой магазин
• Продавать товары
• Принимать заказы
• Получать аналитику

Нажмите кнопку ниже, чтобы начать:
    """)
    
    print("JSON для отправки сообщения:")
    message_data = {
        "chat_id": "USER_ID",  # Замените на реальный ID пользователя
        "text": "Добро пожаловать в Telegram Marketplace! 🛍️\n\nЗдесь вы можете:\n• Создать свой магазин\n• Продавать товары\n• Принимать заказы\n• Получать аналитику\n\nНажмите кнопку ниже, чтобы начать:",
        "reply_markup": keyboard
    }
    print(json.dumps(message_data, indent=2, ensure_ascii=False))
    
    print("\n🔗 Ссылка на бота:")
    print(f"https://t.me/{bot_data['username']}")
    
    print("\n📋 Следующие шаги:")
    print("1. Замените WEB_APP_URL на реальный URL вашего приложения")
    print("2. Разверните приложение на Vercel/Netlify/Render")
    print("3. Протестируйте бота, отправив /start")
    
    return True

def send_test_message(chat_id):
    """Отправка тестового сообщения"""
    
    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🛍️ Открыть Marketplace",
                    "web_app": {"url": WEB_APP_URL}
                }
            ]
        ]
    }
    
    message_data = {
        "chat_id": chat_id,
        "text": "🛍️ Добро пожаловать в Telegram Marketplace!\n\nНажмите кнопку ниже, чтобы открыть приложение:",
        "reply_markup": keyboard
    }
    
    send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(send_url, json=message_data)
    
    if response.status_code == 200:
        print(f"✅ Тестовое сообщение отправлено пользователю {chat_id}")
        return True
    else:
        print(f"❌ Ошибка отправки сообщения: {response.text}")
        return False

if __name__ == "__main__":
    print("🚀 Настройка Telegram Marketplace Bot")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        if len(sys.argv) > 2:
            chat_id = sys.argv[2]
            send_test_message(chat_id)
        else:
            print("❌ Укажите chat_id для тестового сообщения")
            print("Использование: python setup-telegram-bot.py test CHAT_ID")
    else:
        setup_bot()
