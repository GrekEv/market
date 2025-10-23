#!/bin/bash

# 🚀 Скрипт быстрого деплоя Telegram Marketplace

echo "🚀 Деплой Telegram Marketplace"
echo "=============================="

# Проверяем наличие Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI не установлен. Устанавливаем..."
    npm install -g vercel
fi

# Проверяем авторизацию в Vercel
if ! vercel whoami &> /dev/null; then
    echo "🔐 Войдите в Vercel:"
    vercel login
fi

echo ""
echo "📦 Деплой Backend..."
echo "==================="

# Деплой backend
vercel --prod

echo ""
echo "📱 Деплой Frontend..."
echo "===================="

# Переходим в папку client
cd client

# Деплой frontend
vercel --prod

echo ""
echo "✅ Деплой завершен!"
echo ""
echo "📋 Следующие шаги:"
echo "1. Скопируйте URL frontend из вывода выше"
echo "2. Обновите WEB_APP_URL в setup-telegram-bot.py"
echo "3. Запустите: python setup-telegram-bot.py"
echo "4. Протестируйте бота в Telegram"
echo ""
echo "🎉 Готово! Ваш Telegram Mini App развернут!"
