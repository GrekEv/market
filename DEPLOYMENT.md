# 🚀 Инструкция по развертыванию Telegram Marketplace

## 📋 Обзор

Этот проект представляет собой Telegram Mini App - веб-приложение, которое открывается внутри Telegram клиента. Проект состоит из:

- **Frontend**: React приложение (открывается в Telegram)
- **Backend**: Node.js API сервер
- **База данных**: SQLite (для разработки) / PostgreSQL (для продакшена)

## 🎯 Варианты развертывания

### Вариант 1: Vercel (Рекомендуется)

#### 1. Подготовка

```bash
# Установите Vercel CLI
npm i -g vercel

# Войдите в аккаунт Vercel
vercel login
```

#### 2. Деплой Backend

```bash
# Перейдите в корневую директорию проекта
cd telegram-marketplace

# Деплой backend
vercel --prod

# Запомните URL backend (например: https://telegram-marketplace-backend.vercel.app)
```

#### 3. Деплой Frontend

```bash
# Перейдите в папку client
cd client

# Обновите API URL в vercel.json
# Замените "your-backend-url.vercel.app" на реальный URL backend

# Деплой frontend
vercel --prod

# Запомните URL frontend (например: https://telegram-marketplace-frontend.vercel.app)
```

#### 4. Настройка переменных окружения

В панели Vercel добавьте переменные:

**Backend:**
- `TELEGRAM_BOT_TOKEN`: `8206490529:AAEeqvt_x8-Ybpi2QhPW442kg68XVc6V2xE`
- `JWT_SECRET`: `your-super-secret-jwt-key-here-make-it-very-long-and-random`
- `NODE_ENV`: `production`
- `DATABASE_URL`: `file:./dev.db` (для SQLite) или PostgreSQL URL

**Frontend:**
- `REACT_APP_API_URL`: `https://your-backend-url.vercel.app/api`

### Вариант 2: Netlify

#### 1. Деплой Frontend

```bash
# Установите Netlify CLI
npm i -g netlify-cli

# Перейдите в папку client
cd client

# Соберите проект
npm run build

# Деплой
netlify deploy --prod --dir=build
```

#### 2. Деплой Backend

Используйте отдельный сервис для backend (например, Railway, Render, или Heroku).

### Вариант 3: Render

#### 1. Создайте Web Service для Backend

1. Подключите GitHub репозиторий
2. Выберите "Web Service"
3. Настройки:
   - **Build Command**: `cd server && npm install`
   - **Start Command**: `cd server && npm start`
   - **Environment**: `Node`

#### 2. Создайте Static Site для Frontend

1. Выберите "Static Site"
2. Настройки:
   - **Build Command**: `cd client && npm install && npm run build`
   - **Publish Directory**: `client/build`

## 🤖 Настройка Telegram бота

### 1. Обновите URL в скрипте

```bash
# Отредактируйте setup-telegram-bot.py
# Замените WEB_APP_URL на ваш реальный URL frontend
WEB_APP_URL = "https://your-frontend-url.vercel.app"
```

### 2. Запустите скрипт настройки

```bash
# Установите Python зависимости
pip install requests

# Настройте бота
python setup-telegram-bot.py
```

### 3. Протестируйте бота

```bash
# Отправьте тестовое сообщение (замените CHAT_ID на ваш ID)
python setup-telegram-bot.py test YOUR_CHAT_ID
```

## 🔧 Настройка базы данных

### Для продакшена (PostgreSQL)

1. Создайте PostgreSQL базу данных (например, на Railway, Supabase, или Neon)
2. Обновите `DATABASE_URL` в переменных окружения
3. Запустите миграции:

```bash
# На сервере
cd server
npm run migrate
```

### Для разработки (SQLite)

SQLite файл будет создан автоматически при первом запуске.

## 📱 Тестирование Mini App

### 1. Откройте бота в Telegram

```
https://t.me/YOUR_BOT_USERNAME
```

### 2. Нажмите кнопку "Открыть Marketplace"

Приложение должно открыться внутри Telegram клиента.

### 3. Проверьте функциональность

- Регистрация/авторизация
- Создание магазина
- Добавление товаров
- Оформление заказов

## 🛠️ Локальная разработка

### 1. Запуск в режиме разработки

```bash
# Установите зависимости
npm run install:all

# Запустите миграции
cd server && npm run migrate && cd ..

# Запустите проект
npm run dev
```

### 2. Тестирование Mini App локально

1. Используйте ngrok для создания туннеля:

```bash
# Установите ngrok
npm i -g ngrok

# Создайте туннель для frontend
ngrok http 3000

# Создайте туннель для backend
ngrok http 5000
```

2. Обновите URL в `setup-telegram-bot.py`
3. Настройте бота с новыми URL

## 🔒 Безопасность

### 1. Переменные окружения

Никогда не коммитьте:
- `.env` файлы
- Токены ботов
- Секретные ключи
- URL базы данных

### 2. HTTPS

Убедитесь, что все URL используют HTTPS в продакшене.

### 3. Валидация данных

Все данные от Telegram Web App должны быть валидированы на сервере.

## 📊 Мониторинг

### 1. Логи

Настройте логирование для отслеживания ошибок:
- Vercel: автоматические логи
- Render: встроенные логи
- Railway: логи в панели

### 2. Аналитика

Добавьте Google Analytics или другую аналитику для отслеживания использования.

## 🚨 Устранение неполадок

### 1. Mini App не открывается

- Проверьте, что URL доступен по HTTPS
- Убедитесь, что Telegram Web App скрипт загружается
- Проверьте консоль браузера на ошибки

### 2. API не работает

- Проверьте CORS настройки
- Убедитесь, что переменные окружения установлены
- Проверьте логи сервера

### 3. База данных

- Убедитесь, что миграции выполнены
- Проверьте подключение к базе данных
- Проверьте права доступа

## 📞 Поддержка

При возникновении проблем:

1. Проверьте логи приложения
2. Убедитесь, что все переменные окружения установлены
3. Проверьте доступность всех URL
4. Протестируйте API endpoints

## 🎉 Готово!

После выполнения всех шагов у вас будет:

- ✅ Развернутое Telegram Mini App
- ✅ Настроенный Telegram бот
- ✅ Работающий API
- ✅ База данных

Пользователи смогут открывать ваше приложение прямо в Telegram и использовать все функции маркетплейса!
