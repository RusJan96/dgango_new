
# TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'
# бот через deepseek 
# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     CallbackQueryHandler,
#     ContextTypes,
#     MessageHandler,
#     filters
# )

# # Настройка логирования
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'  # Замените на реальный токен

# # Моковые данные автосервисов
# AUTO_SERVICES = {
#     'toyota': {
#         'maintenance': [
#             {'name': 'Toyota Center', 'rating': 9.8, 'price': 5000},
#             {'name': 'Toyota Pro', 'rating': 9.5, 'price': 4500}
#         ],
#         'body': [
#             {'name': 'Toyota Body Repair', 'rating': 9.2, 'price': 12000},
#             {'name': 'Elite Toyota', 'rating': 9.0, 'price': 10000}
#         ]
#     }, 
#     'bmw': {
#         'maintenance': [
#             {'name': 'BMW Service', 'rating': 9.7, 'price': 7000},
#             {'name': 'BMW Premium', 'rating': 9.6, 'price': 6500}
#         ],
#         'body': [
#             {'name': 'BMW Body Masters', 'rating': 9.4, 'price': 15000},
#             {'name': 'BMW Exclusive', 'rating': 9.3, 'price': 14000}
#         ]
#     }
# }

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Обработчик команды /start"""
#     keyboard = [
#         [InlineKeyboardButton("🛠️ Зарегистрировать Автосервис", callback_data='register')],
#         [InlineKeyboardButton("🔍 Подобрать автосервис", callback_data='find')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     if update.message:
#         await update.message.reply_text(
#             "Привет! Я бот для подбора автосервисов. Как я могу помочь?",
#             reply_markup=reply_markup
#         )
#     elif update.callback_query:
#         await update.callback_query.message.reply_text(
#             "Привет! Я бот для подбора автосервисов. Как я могу помочь?",
#             reply_markup=reply_markup
#         )

# async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Обработчик нажатий на кнопки"""
#     query = update.callback_query
#     await query.answer()
    
#     if query.data == 'back_to_start':
#         await start(update, context)
#     elif query.data == 'register':
#         await handle_register(query)
#     elif query.data == 'find':
#         await select_car_brand(query, context)
#     elif query.data.startswith('brand_'):
#         await select_repair_type(query, context)
#     elif query.data.startswith('repair_'):
#         await show_services(query, context)

# async def handle_register(query):
#     """Обработчик регистрации автосервиса"""
#     keyboard = [
#         [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await query.edit_message_text(
#         "📝 Для регистрации автосервиса свяжитесь с администратором: @admin_username\n\n"
#         "Пожалуйста, укажите в сообщении:\n"
#         "- Название автосервиса\n"
#         "- Адрес\n"
#         "- Контактные данные\n"
#         "- Специализацию",
#         reply_markup=reply_markup
#     )

# async def select_car_brand(query, context):
#     """Выбор марки автомобиля"""
#     keyboard = [
#         [InlineKeyboardButton("Toyota", callback_data='brand_toyota')],
#         [InlineKeyboardButton("BMW", callback_data='brand_bmw')],
#         [InlineKeyboardButton("Audi", callback_data='brand_audi')],
#         [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(
#         "🚗 Выберите марку автомобиля:",
#         reply_markup=reply_markup
#     )

# async def select_repair_type(query, context):
#     """Выбор типа ремонта"""
#     brand = query.data.split('_')[1]
#     context.user_data['brand'] = brand
    
#     keyboard = [
#         [InlineKeyboardButton("🛠️ Техническое обслуживание", callback_data='repair_maintenance')],
#         [InlineKeyboardButton("🚘 Кузовной ремонт", callback_data='repair_body')],
#         [InlineKeyboardButton("🔙 Назад", callback_data='find')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(
#         f"Вы выбрали {brand.capitalize()}. Теперь выберите тип работ:",
#         reply_markup=reply_markup
#     )

# async def show_services(query, context):
#     """Показать список автосервисов"""
#     brand = context.user_data.get('brand', '')
#     repair_type = query.data.split('_')[1]
    
#     services = AUTO_SERVICES.get(brand, {}).get(repair_type, [])
    
#     if not services:
#         keyboard = [
#             [InlineKeyboardButton("🔙 Назад", callback_data=f'brand_{brand}')]
#         ]
#         reply_markup = InlineKeyboardMarkup(keyboard)
        
#         await query.edit_message_text(
#             "😕 К сожалению, нет доступных автосервисов по вашему запросу.",
#             reply_markup=reply_markup
#         )
#         return
    
#     services_sorted = sorted(services, key=lambda x: x['rating'], reverse=True)
    
#     services_text = "\n\n".join(
#         f"🔹 {s['name']}\n"
#         f"⭐ Рейтинг: {s['rating']}/10\n"
#         f"💵 Стоимость: от {s['price']} руб."
#         for s in services_sorted
#     )
    
#     keyboard = [
#         [InlineKeyboardButton("🔙 Назад", callback_data=f'brand_{brand}')],
#         [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await query.edit_message_text(
#         f"🔧 Автосервисы для {brand.capitalize()} ({repair_type}):\n\n{services_text}",
#         reply_markup=reply_markup
#     )

# async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Обработчик ошибок"""
#     logger.error(f"Ошибка: {context.error}", exc_info=context.error)
#     if update.callback_query:
#         await update.callback_query.message.reply_text("⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.")

# def main():
#     """Запуск бота"""
#     application = Application.builder().token(TOKEN).build()
    
#     # Регистрация обработчиков
#     application.add_handler(CommandHandler('start', start))
#     application.add_handler(CallbackQueryHandler(handle_button))
#     application.add_error_handler(error_handler)
    
#     logger.info("Бот запущен и ожидает сообщений...")
#     application.run_polling()

# if __name__ == '__main__':
#     main()

# import logging
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     CallbackQueryHandler,
#     ContextTypes,
#     MessageHandler,
#     filters,
#     ConversationHandler
# )

# # Настройка логирования
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'
# ADMIN_CHAT_ID = '123456789'  # Замените на реальный chat_id администратора

# # Состояния для регистрации автосервиса
# NAME, SERVICES, PRICES, ADDRESS, PHONE, CONFIRM = range(6)

# # ... (остальные переменные и функции остаются такими же, как в предыдущем коде)

# async def start_registration(query, context):
#     """Начало процесса регистрации автосервиса"""
#     context.user_data['registration'] = {}
    
#     keyboard = [[InlineKeyboardButton("❌ Отмена", callback_data='back_to_start')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await query.edit_message_text(
#         "📝 <b>Регистрация автосервиса</b>\n\n"
#         "Пожалуйста, введите <b>название</b> вашего автосервиса:",
#         reply_markup=reply_markup,
#         parse_mode='HTML'
#     )
    
#     return NAME

# async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Получение названия автосервиса"""
#     context.user_data['registration']['name'] = update.message.text
    
#     await update.message.reply_text(
#         "🛠️ Введите <b>виды работ</b>, которые выполняет ваш автосервис (через запятую):\n\n"
#         "Пример: Замена масла, Ремонт подвески, Диагностика",
#         parse_mode='HTML'
#     )
    
#     return SERVICES

# async def get_services(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Получение видов работ"""
#     services = [s.strip() for s in update.message.text.split(',')]
#     context.user_data['registration']['services'] = services
    
#     await update.message.reply_text(
#         "💰 Теперь введите <b>цены</b> для каждого вида работ (в том же порядке, через запятую):\n\n"
#         "Пример: 1500, 2000, 1000",
#         parse_mode='HTML'
#     )
    
#     return PRICES

# async def get_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Получение цен на работы"""
#     prices = [p.strip() for p in update.message.text.split(',')]
#     services = context.user_data['registration']['services']
    
#     if len(prices) != len(services):
#         await update.message.reply_text(
#             "❌ Количество цен не совпадает с количеством видов работ. "
#             "Пожалуйста, введите цены еще раз:",
#             parse_mode='HTML'
#         )
#         return PRICES
    
#     # Собираем услуги и цены в словарь
#     services_prices = dict(zip(services, prices))
#     context.user_data['registration']['services_prices'] = services_prices
    
#     await update.message.reply_text(
#         "🏠 Теперь введите <b>адрес</b> вашего автосервиса:",
#         parse_mode='HTML'
#     )
    
#     return ADDRESS

# async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Получение адреса автосервиса"""
#     context.user_data['registration']['address'] = update.message.text
    
#     await update.message.reply_text(
#         "📱 Введите <b>номер телефона</b> для связи:",
#         parse_mode='HTML'
#     )
    
#     return PHONE

# async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Получение номера телефона"""
#     context.user_data['registration']['phone'] = update.message.text
    
#     # Формируем сводку данных для подтверждения
#     registration_data = context.user_data['registration']
#     services_text = "\n".join(
#         f"• {service}: {price} руб." 
#         for service, price in registration_data['services_prices'].items()
#     )
    
#     summary_text = (
#         "📋 <b>Проверьте введенные данные:</b>\n\n"
#         f"🏢 <b>Название:</b> {registration_data['name']}\n"
#         f"🛠️ <b>Услуги и цены:</b>\n{services_text}\n"
#         f"🏠 <b>Адрес:</b> {registration_data['address']}\n"
#         f"📱 <b>Телефон:</b> {registration_data['phone']}\n\n"
#         "Всё верно?"
#     )
    
#     keyboard = [
#         [InlineKeyboardButton("✅ Да, зарегистрировать", callback_data='confirm_registration')],
#         [InlineKeyboardButton("❌ Нет, начать заново", callback_data='restart_registration')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
    
#     await update.message.reply_text(
#         text=summary_text,
#         reply_markup=reply_markup,
#         parse_mode='HTML'
#     )
    
#     return CONFIRM

# async def confirm_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Подтверждение регистрации"""
#     query = update.callback_query
#     await query.answer()
    
#     if query.data == 'confirm_registration':
#         registration_data = context.user_data['registration']
        
#         # Формируем сообщение для администратора
#         services_text = "\n".join(
#             f"• {service}: {price} руб." 
#             for service, price in registration_data['services_prices'].items()
#         )
        
#         admin_message = (
#             "📝 <b>Новая заявка на регистрацию автосервиса</b>\n\n"
#             f"🏢 Название: {registration_data['name']}\n"
#             f"🏠 Адрес: {registration_data['address']}\n"
#             f"📞 Телефон: {registration_data['phone']}\n\n"
#             f"🛠️ <b>Услуги и цены:</b>\n{services_text}\n\n"
#             f"ID пользователя: {update.effective_user.id}\n"
#             f"Username: @{update.effective_user.username if update.effective_user.username else 'не указан'}"
#         )
        
#         # Отправляем сообщение администратору
#         try:
#             await context.bot.send_message(
#                 chat_id=ADMIN_CHAT_ID,
#                 text=admin_message,
#                 parse_mode='HTML'
#             )
            
#             keyboard = [
#                 [InlineKeyboardButton("🆘 Поддержка", callback_data='support')],
#                 [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]
#             ]
#             reply_markup = InlineKeyboardMarkup(keyboard)
            
#             await query.edit_message_text(
#                 "✅ <b>Спасибо за регистрацию!</b>\n\n"
#                 "Ваши данные отправлены администратору. Для завершения регистрации "
#                 "и добавления вашего автосервиса в нашу базу свяжитесь с администратором: @admin_username",
#                 reply_markup=reply_markup,
#                 parse_mode='HTML'
#             )
            
#         except Exception as e:
#             logger.error(f"Ошибка при отправке сообщения администратору: {e}")
#             await query.edit_message_text(
#                 "⚠️ Произошла ошибка при отправке данных. Пожалуйста, попробуйте позже или свяжитесь с поддержкой.",
#                 parse_mode='HTML'
#             )
    
#     elif query.data == 'restart_registration':
#         await start_registration(query, context)
    
#     return ConversationHandler.END

# def main():
#     """Запуск бота"""
#     application = Application.builder().token(TOKEN).build()
    
#     # Обработчик регистрации
#     conv_handler = ConversationHandler(
#         entry_points=[CallbackQueryHandler(start_registration, pattern='^register_service$')],
#         states={
#             NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
#             SERVICES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_services)],
#             PRICES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_prices)],
#             ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_address)],
#             PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
#             CONFIRM: [CallbackQueryHandler(confirm_registration, pattern='^(confirm_registration|restart_registration)$')]
#         },
#         fallbacks=[
#             CommandHandler('cancel', cancel_registration),
#             CallbackQueryHandler(cancel_registration, pattern='^back_to_start$')
#         ]
#     )
    
#     # Регистрация обработчиков
#     application.add_handler(CommandHandler('start', start))
#     application.add_handler(conv_handler)
#     application.add_handler(CallbackQueryHandler(handle_button))
#     application.add_error_handler(error_handler)
    
#     logger.info("Бот запущен и ожидает сообщений...")
#     application.run_polling()

# if __name__ == '__main__':
#     main()

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ConversationHandler
)

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = '7942582757:AAHhO_vAUbO9_D0kpAIiq0SzOBUXNwcUsxY'
ADMIN_USERNAME = '@Batojan'  # Username администратора и поддержки

# Состояния для регистрации автосервиса
NAME, SERVICES, PRICES, ADDRESS, PHONE = range(5)

# Данные автосервисов (пример)
AUTO_SERVICES = {
    'AutoFRESH': {
        'rating': 9.7,
        'address': 'г. Красноярск, ул. Караульная 9/2',
        'phone': '+7 (391) 123-45-67',
        'services': {
            'Автоэлектрик': 1000,
            'Ремонт подвески': 700,
            'Замена масла': 1350
        }
    },
    'Skoda Auto': {
        'rating': 9.9,
        'address': 'г. Красноярск, ул. 9 Мая А72',
        'phone': '+7 (391) 987-65-43',
        'services': {
            'Ремонт подвески': 600,
            'Замена масла в коробке передач': 1700
        }
    }
}

# Виды ремонта с описанием
REPAIR_TYPES = {
    'Все виды ремонта': 'Комплексный ремонт любой сложности',
    'Автоэлектрик': 'Диагностика и ремонт электрооборудования',
    'Ремонт подвески': 'Диагностика и ремонт подвески',
    'Замена масла': 'Замена масла в двигателе',
    'Замена масла в коробке передач': 'Замена масла в АКПП/МКПП',
    'Диагностика': 'Компьютерная диагностика автомобиля',
    'Ремонт двигателя': 'Капитальный и текущий ремонт ДВС'
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    keyboard = [
        [InlineKeyboardButton("🔍 Найти автосервис", callback_data='find_service')],
        [InlineKeyboardButton("📝 Зарегистрировать автосервис", callback_data='register_service')],
        [InlineKeyboardButton("🆘 Поддержка", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    user = update.effective_user
    welcome_message = (
        f"🚗 <b>Добро пожаловать, {user.first_name}!</b>\n\n"
        "Я помогу вам найти подходящий автосервис в Красноярске "
        "или зарегистрировать свой сервис в нашей базе."
    )
    
    if update.message:
        await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='HTML')
    else:
        await update.callback_query.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='HTML')

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    try:
        if query.data == 'back_to_start':
            await start(update, context)
        elif query.data == 'find_service':
            await show_repair_types(query, context)
        elif query.data == 'register_service':
            await start_registration(query, context)
        elif query.data == 'support':
            await show_support(query)
        elif query.data.startswith('repair_'):
            repair_type = query.data.split('_')[1]
            await show_services_for_repair(query, context, repair_type)
        elif query.data.startswith('service_'):
            service_name = query.data.split('_')[1]
            repair_type = context.user_data.get('current_repair_type', '')
            await show_service_details(query, context, service_name, repair_type)
    except Exception as e:
          logger.error(f"Ошибка в handle_button: {e}", exc_info=True)
          await query.edit_message_text(
           "⚠️ Произошла ошибка. Пожалуйста, попробуйте позже.",
           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]])
        )

async def show_support(query):
    """Показать информацию о поддержке"""
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"🆘 <b>Поддержка</b>\n\n"
        f"Если у вас возникли вопросы или проблемы, "
        f"свяжитесь с администратором: {ADMIN_USERNAME}\n\n"
        "Мы постараемся помочь вам как можно скорее!",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def show_repair_types(query, context):
    """Показать виды ремонта"""
    keyboard = []
    for repair_type in REPAIR_TYPES:
        keyboard.append([InlineKeyboardButton(f"🔧 {repair_type}", callback_data=f'repair_{repair_type}')])
    
    keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data='back_to_start')])
    keyboard.append([InlineKeyboardButton("🆘 Поддержка", callback_data='support')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "🛠️ <b>Выберите тип необходимых работ:</b>\n\n"
        "Укажите, какие работы вам нужно выполнить, и мы подберем подходящие автосервисы.",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def show_services_for_repair(query, context, repair_type):
    """Показать автосервисы для выбранного вида ремонта"""
    context.user_data['current_repair_type'] = repair_type
    
    suitable_services = [
        (name, info) for name, info in AUTO_SERVICES.items() 
        if repair_type in info['services']
    ]
    
    if not suitable_services:
        keyboard = [
            [InlineKeyboardButton("🔙 Назад", callback_data='find_service')],
            [InlineKeyboardButton("🆘 Поддержка", callback_data='support')],
            [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            f"😕 <b>Нет доступных автосервисов</b>\n\n"
            f"К сожалению, в нашей базе нет автосервисов, предоставляющих услугу '{repair_type}'.\n\n"
            f"Вы можете:\n"
            f"• Попробовать выбрать другой вид работ\n"
            f"• Оставить заявку на добавление своего автосервиса\n"
            f"• Связаться с поддержкой {ADMIN_USERNAME}",
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
        return
    
    keyboard = []
    for service_name, service_info in suitable_services:
        price = service_info['services'][repair_type]
        keyboard.append([InlineKeyboardButton(
            f"🏢 {service_name} ⭐ {service_info['rating']} - от {price} руб.",
            callback_data=f'service_{service_name}'
        )])
    
    keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data='find_service')])
    keyboard.append([InlineKeyboardButton("🆘 Поддержка", callback_data='support')])
    keyboard.append([InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"🔧 <b>Автосервисы, выполняющие {repair_type}:</b>\n\n"
        f"<i>{REPAIR_TYPES.get(repair_type, '')}</i>\n\n"
        f"Выберите автосервис для просмотра подробной информации:",
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def show_service_details(query, context, service_name, repair_type):
    """Показать детали автосервиса"""
    service_info = AUTO_SERVICES.get(service_name, {})
    price = service_info.get('services', {}).get(repair_type, 'не указана')
    
    text = (
        f"🏢 <b>{service_name}</b>\n"
        f"⭐ Рейтинг: {service_info.get('rating', 'нет')}/10\n"
        f"🏠 Адрес: {service_info.get('address', 'не указан')}\n"
        f"📞 Телефон: {service_info.get('phone', 'не указан')}\n\n"
        f"🔧 <b>{repair_type}</b>\n"
        f"💵 Стоимость: от {price} руб.\n\n"
        f"<i>{REPAIR_TYPES.get(repair_type, '')}</i>"
    )
    
    keyboard = [
        [InlineKeyboardButton("🔙 Назад", callback_data=f'repair_{repair_type}')],
        [InlineKeyboardButton("🆘 Поддержка", callback_data='support')],
        [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode='HTML')

# Регистрация автосервиса
async def start_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Начало процесса регистрации автосервиса"""
    try:
        query = update.callback_query
        await query.answer()
        
        context.user_data['registration'] = {}
        keyboard = [[InlineKeyboardButton("❌ Отмена", callback_data='back_to_start')]]
        
        await query.edit_message_text(
            "📝 <b>Регистрация автосервиса</b>\n\n"
            "Пожалуйста, введите <b>название</b> вашего автосервиса:",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        return NAME
    except Exception as e:
        logger.error(f"Ошибка в start_registration: {e}", exc_info=True)
        
        # Отправляем новое сообщение об ошибке
        if update.callback_query:
            await update.callback_query.message.reply_text(
                "⚠️ Произошла ошибка при начале регистрации. Пожалуйста, попробуйте позже.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]])
            )
        else:
            await update.message.reply_text(
                "⚠️ Произошла ошибка при начале регистрации. Пожалуйста, попробуйте позже.",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')]])
            )
        return ConversationHandler.END

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Получение названия автосервиса"""
    try:
        context.user_data['registration']['name'] = update.message.text
        await update.message.reply_text(
            "🛠️ Введите <b>виды работ</b>, которые выполняет ваш автосервис (через запятую):\n\n"
            "Пример: Замена масла, Ремонт подвески, Диагностика",
            parse_mode='HTML'
        )
        return SERVICES
    except Exception as e:
        logger.error(f"Ошибка в get_name: {e}", exc_info=True)
        await handle_registration_error(update, context)
        return ConversationHandler.END

async def get_services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Получение видов работ"""
    try:
        services = [s.strip() for s in update.message.text.split(',')]
        context.user_data['registration']['services'] = services
        await update.message.reply_text(
            "💰 Теперь введите <b>цены</b> для каждого вида работ (в том же порядке, через запятую):\n\n"
            "Пример: 1500, 2000, 1000",
            parse_mode='HTML'
        )
        return PRICES
    except Exception as e:
        logger.error(f"Ошибка в get_services: {e}", exc_info=True)
        await handle_registration_error(update, context)
        return ConversationHandler.END

async def get_prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Получение цен на работы"""
    try:
        prices = [p.strip() for p in update.message.text.split(',')]
        services = context.user_data['registration']['services']
        
        if len(prices) != len(services):
            await update.message.reply_text(
                "❌ Количество цен не совпадает с количеством видов работ. "
                "Пожалуйста, введите цены еще раз:",
                parse_mode='HTML'
            )
            return PRICES
        
        context.user_data['registration']['services_prices'] = dict(zip(services, prices))
        await update.message.reply_text("🏠 Теперь введите <b>адрес</b> вашего автосервиса:", parse_mode='HTML')
        return ADDRESS
    except Exception as e:
        logger.error(f"Ошибка в get_prices: {e}", exc_info=True)
        await handle_registration_error(update, context)
        return ConversationHandler.END

async def get_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Получение адреса автосервиса"""
    try:
        context.user_data['registration']['address'] = update.message.text
        await update.message.reply_text("📱 Введите <b>номер телефона</b> для связи:", parse_mode='HTML')
        return PHONE
    except Exception as e:
        logger.error(f"Ошибка в get_address: {e}", exc_info=True)
        await handle_registration_error(update, context)
        return ConversationHandler.END

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Завершение регистрации"""
    try:
        context.user_data['registration']['phone'] = update.message.text
        registration_data = context.user_data['registration']
        
        # Формируем сообщение для администратора
        services_text = "\n".join(
            f"• {service}: {price} руб." 
            for service, price in registration_data['services_prices'].items()
        )
        
        admin_message = (
            "📝 <b>Новая заявка на регистрацию автосервиса</b>\n\n"
            f"🏢 Название: {registration_data['name']}\n"
            f"🏠 Адрес: {registration_data['address']}\n"
            f"📞 Телефон: {registration_data['phone']}\n\n"
            f"🛠️ <b>Услуги и цены:</b>\n{services_text}\n\n"
            f"ID пользователя: {update.effective_user.id}\n"
            f"Username: @{update.effective_user.username or 'не указан'}"
        )
        
        # Отправляем сообщение администратору через username
        await context.bot.send_message(
            chat_id=ADMIN_USERNAME,
            text=admin_message,
            parse_mode='HTML'
        )
        
        keyboard = [
            [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')],
            [InlineKeyboardButton("🆘 Поддержка", callback_data='support')]
        ]
        
        await update.message.reply_text(
            f"✅ <b>Спасибо за регистрацию!</b>\n\n"
            f"Ваши данные отправлены администратору {ADMIN_USERNAME}. "
            "Для завершения регистрации свяжитесь с администратором.",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode='HTML'
        )
        
        logger.info(f"Новая заявка на регистрацию: {registration_data}")
        return ConversationHandler.END
    except Exception as e:
        logger.error(f"Ошибка в get_phone: {e}", exc_info=True)
        await handle_registration_error(update, context)
        return ConversationHandler.END

async def handle_registration_error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка ошибок при регистрации"""
    if 'registration' in context.user_data:
        del context.user_data['registration']
    
    keyboard = [
        [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')],
        [InlineKeyboardButton("🆘 Поддержка", callback_data='support')]
    ]
    
    if update.message:
        await update.message.reply_text(
            "⚠️ Произошла ошибка при регистрации. Пожалуйста, попробуйте позже.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif update.callback_query:
        await update.callback_query.message.reply_text(
            "⚠️ Произошла ошибка при регистрации. Пожалуйста, попробуйте позже.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def cancel_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отмена регистрации"""
    if 'registration' in context.user_data:
        del context.user_data['registration']
    
    keyboard = [
        [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')],
        [InlineKeyboardButton("🆘 Поддержка", callback_data='support')]
    ]
    
    await update.message.reply_text(
        "Регистрация автосервиса отменена.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    
    return ConversationHandler.END

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Ошибка: {context.error}", exc_info=context.error)
    
    keyboard = [
        [InlineKeyboardButton("🏠 В начало", callback_data='back_to_start')],
        [InlineKeyboardButton("🆘 Поддержка", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    error_message = "⚠️ Произошла ошибка. Пожалуйста, попробуйте позже."
    
    if update.callback_query:
        await update.callback_query.message.reply_text(error_message, reply_markup=reply_markup)
    elif update.message:
        await update.message.reply_text(error_message, reply_markup=reply_markup)

def main():
    """Запуск бота"""
    application = Application.builder().token(TOKEN).build()
    
    # Обработчик регистрации
    conv_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(start_registration, pattern='^register_service$'),
            CommandHandler('register', start_registration)  # Добавляем обработчик команды /register
        ],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            SERVICES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_services)],
            PRICES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_prices)],
            ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_address)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)]
        },
        fallbacks=[
            CommandHandler('cancel', cancel_registration),
            CallbackQueryHandler(cancel_registration, pattern='^back_to_start$')
        ]
    )
    
    # Регистрация обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(handle_button))
    application.add_error_handler(error_handler)
    
    logger.info("Бот запущен и ожидает сообщений...")
    application.run_polling()
if __name__ == '__main__':
    main()