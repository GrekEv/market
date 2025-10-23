# 🛍️ Telegram Marketplace

Telegram Mini App для блогеров - продавайте товары и цифровые активы прямо в Telegram!

## ✨ Возможности

- 🏪 **Создание магазина** - Создайте свой собственный магазин в Telegram
- 📦 **Управление товарами** - Добавляйте физические и цифровые товары
- 💰 **Прием заказов** - Получайте заказы от покупателей
- 💳 **Платежи** - Интеграция с Telegram Stars и другими способами оплаты
- 📊 **Аналитика** - Отслеживайте продажи и статистику
- ⭐ **Отзывы** - Система отзывов и рейтингов
- 💬 **Сообщения** - Общение с покупателями
- 🔐 **Безопасность** - Telegram авторизация и защита данных

## 🚀 Быстрый старт

### 1. Локальная разработка

```bash
# Клонируйте репозиторий
git clone <your-repo-url>
cd telegram-marketplace

# Установите зависимости
npm run install:all

# Настройте базу данных
npm run setup:quick

# Запустите проект
npm run dev
```

Приложение будет доступно:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

### 2. Деплой в продакшен

```bash
# Автоматический деплой на Vercel
npm run deploy

# Или следуйте подробной инструкции в DEPLOYMENT.md
```

### 3. Настройка Telegram бота

```bash
# Настройте бота с вашим токеном
npm run setup:bot

# Отправьте тестовое сообщение
npm run test:bot YOUR_CHAT_ID
```

## 📱 Как это работает

1. **Пользователь нажимает кнопку** в Telegram боте
2. **Открывается Mini App** внутри Telegram клиента
3. **Авторизация** происходит автоматически через Telegram
4. **Пользователь использует** все функции маркетплейса
5. **Данные сохраняются** в базе данных

## 🛠️ Технологии

### Frontend
- React 18
- Tailwind CSS
- Telegram Web App API
- React Router
- Zustand (состояние)

### Backend
- Node.js
- Express.js
- SQLite/PostgreSQL
- JWT авторизация
- Telegram Bot API

### Инфраструктура
- Vercel (деплой)
- SQLite (разработка)
- PostgreSQL (продакшен)

## 📁 Структура проекта

```
telegram-marketplace/
├── client/                 # React приложение
│   ├── src/
│   │   ├── components/     # React компоненты
│   │   ├── pages/         # Страницы приложения
│   │   ├── contexts/      # React контексты
│   │   └── services/      # API сервисы
│   └── public/
├── server/                # Node.js сервер
│   ├── routes/           # API маршруты
│   ├── middleware/       # Middleware
│   ├── migrations/       # Миграции БД
│   └── utils/           # Утилиты
├── setup-telegram-bot.py # Скрипт настройки бота
├── deploy.sh            # Скрипт деплоя
└── DEPLOYMENT.md        # Инструкция по деплою
```

## 🔧 Конфигурация

### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# Telegram Bot
TELEGRAM_BOT_TOKEN=your_bot_token_here

# JWT Secret
JWT_SECRET=your_super_secret_jwt_key

# Database
NODE_ENV=development
DATABASE_URL=./server/dev.db

# Server
PORT=5000
```

### Настройка бота

1. Создайте бота через [@BotFather](https://t.me/botfather)
2. Получите токен бота
3. Обновите `TELEGRAM_BOT_TOKEN` в `.env`
4. Запустите `npm run setup:bot`

## 📊 API Endpoints

### Аутентификация
- `POST /api/auth/telegram` - Авторизация через Telegram
- `GET /api/auth/me` - Получение данных пользователя

### Магазины
- `GET /api/shops` - Список магазинов
- `POST /api/shops/apply` - Подача заявки на магазин
- `GET /api/shops/:id` - Информация о магазине

### Товары
- `GET /api/products` - Список товаров
- `POST /api/products` - Создание товара
- `PUT /api/products/:id` - Обновление товара

### Заказы
- `GET /api/orders` - Список заказов
- `POST /api/orders` - Создание заказа
- `PUT /api/orders/:id` - Обновление заказа

## 🎨 Кастомизация

### Темы
Приложение автоматически адаптируется под тему Telegram:
- Светлая тема
- Темная тема
- Системная тема

### Стили
Используйте Tailwind CSS для кастомизации:
```css
/* Пример кастомных стилей */
.custom-button {
  @apply bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded;
}
```

## 🔒 Безопасность

- ✅ Telegram Web App авторизация
- ✅ JWT токены
- ✅ Валидация данных
- ✅ Rate limiting
- ✅ CORS настройки
- ✅ SQL injection защита

## 📈 Мониторинг

### Логи
- Серверные логи в консоли
- Ошибки в базе данных
- Security events

### Аналитика
- Отслеживание пользователей
- Статистика продаж
- Популярные товары

## 🚨 Устранение неполадок

### Mini App не открывается
1. Проверьте HTTPS URL
2. Убедитесь, что Telegram Web App скрипт загружается
3. Проверьте консоль браузера

### API не работает
1. Проверьте CORS настройки
2. Убедитесь в правильности переменных окружения
3. Проверьте логи сервера

### База данных
1. Убедитесь, что миграции выполнены
2. Проверьте подключение к БД
3. Проверьте права доступа

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте feature branch
3. Внесите изменения
4. Создайте Pull Request

## 📄 Лицензия

MIT License - см. файл [LICENSE](LICENSE)

## 📞 Поддержка

- 📧 Email: support@example.com
- 💬 Telegram: [@your_support_bot](https://t.me/your_support_bot)
- 🐛 Issues: [GitHub Issues](https://github.com/your-repo/issues)

## 🎉 Благодарности

- Telegram за Web App API
- React команда за отличный фреймворк
- Vercel за простой деплой
- Всем контрибьюторам проекта

---

**Сделано с ❤️ для Telegram сообщества**
