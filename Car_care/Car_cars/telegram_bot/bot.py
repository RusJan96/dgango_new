
# TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'
# бот через deepseek 
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'  # Замените на реальный токен

# Моковые данные автосервисов
AUTO_SERVICES = {
    'toyota': {
        'maintenance': [
            {'name': 'Toyota Center', 'rating': 9.8, 'price': 5000},
            {'name': 'Toyota Pro', 'rating': 9.5, 'price': 4500}
        ],
        'body': [
            {'name': 'Toyota Body Repair', 'rating': 9.2, 'price': 12000},
            {'name': 'Elite Toyota', 'rating': 9.0, 'price': 10000}
        ]
    }, 
    'bmw': {
        'maintenance': [
            {'name': 'BMW Service', 'rating': 9.7, 'price': 7000},
            {'name': 'BMW Premium', 'rating': 9.6, 'price': 6500}
        ],
        'body': [
            {'name': 'BMW Body Masters', 'rating': 9.4, 'price': 15000},
            {'name': 'BMW Exclusive', 'rating': 9.3, 'price': 14000}
        ]
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    keyboard = [
        [InlineKeyboardButton("🛠️ Зарегистрировать Автосервис", callback_data='register')],
        [InlineKeyboardButton("🔍 Подобрать автосервис", callback_data='find')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(
            "Привет! Я бот для подбора автосервисов. Как я могу помочь?",
            reply_markup=reply_markup
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            "Привет! Я бот для подбора автосервисов. Как я могу помочь?",
            reply_markup=reply_markup
        )

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'back_to_start':
        await start(update, context)
    elif query.data == 'register':
        await handle_register(query)
    elif query.data == 'find':
        await select_car_brand(query, context)
    elif query.data.startswith('brand_'):
        await select_repair_type(query, context)
    elif query.data.startswith('repair_'):
        await show_services(query, context)

async def handle_register(query):
    """Обработчик регистрации автосервиса"""
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "📝 Для регистрации автосервиса свяжитесь с администратором: @admin_username\n\n"
        "Пожалуйста, укажите в сообщении:\n"
        "- Название автосервиса\n"
        "- Адрес\n"
        "- Контактные данные\n"
        "- Специализацию",
        reply_markup=reply_markup
    )

async def select_car_brand(query, context):
    """Выбор марки автомобиля"""
    keyboard = [
        [InlineKeyboardButton("Toyota", callback_data='brand_toyota')],
        [InlineKeyboardButton("BMW", callback_data='brand_bmw')],
        [InlineKeyboardButton("Audi", callback_data='brand_audi')],
        [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        "🚗 Выберите марку автомобиля:",
        reply_markup=reply_markup
    )

async def select_repair_type(query, context):
    """Выбор типа ремонта"""
    brand = query.data.split('_')[1]
    context.user_data['brand'] = brand
    
    keyboard = [
        [InlineKeyboardButton("🛠️ Техническое обслуживание", callback_data='repair_maintenance')],
        [InlineKeyboardButton("🚘 Кузовной ремонт", callback_data='repair_body')],
        [InlineKeyboardButton("🔙 Назад", callback_data='find')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        f"Вы выбрали {brand.capitalize()}. Теперь выберите тип работ:",
        reply_markup=reply_markup
    )

async def show_services(query, context):
    """Показать список автосервисов"""
    brand = context.user_data.get('brand', '')
    repair_type = query.data.split('_')[1]
    
    services = AUTO_SERVICES.get(brand, {}).get(repair_type, [])
    
    if not services:
        keyboard = [
            [InlineKeyboardButton("🔙 Назад", callback_data=f'brand_{brand}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "😕 К сожалению, нет доступных автосервисов по вашему запросу.",
            reply_markup=reply_markup
        )
        return
    
    services_sorted = sorted(services, key=lambda x: x['rating'], reverse=True)
    
    services_text = "\n\n".join(
        f"🔹 {s['name']}\n"
        f"⭐ Рейтинг: {s['rating']}/10\n"
        f"💵 Стоимость: от {s['price']} руб."
        for s in services_sorted
    )
    
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data=f'brand_{brand}')],
        [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"🔧 Автосервисы для {brand.capitalize()} ({repair_type}):\n\n{services_text}",
        reply_markup=reply_markup
    )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Ошибка: {context.error}", exc_info=context.error)
    if update.callback_query:
        await update.callback_query.message.reply_text("⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")

def main():
    """Запуск бота"""
    application = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(handle_button))
    application.add_error_handler(error_handler)
    
    logger.info("Бот запущен и ожидает сообщений...")
    application.run_polling()

if __name__ == '__main__':
    main()