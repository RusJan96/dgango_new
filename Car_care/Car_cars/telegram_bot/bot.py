# telegram_bot/bot.py
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from django.core.management.base import BaseCommand
from django.conf import settings

# Включаем логирование для отладки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для подбора автосервисов. Как я могу помочь?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Пока я умею только здороваться. Но скоро я стану полезнее!")

def main():
    token = settings.TELEGRAM_BOT_TOKEN  # Токен вашего бота
    application = ApplicationBuilder().token(token).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    # Запуск бота
    application.run_polling()

class Command(BaseCommand):
    help = 'Запустить Telegram бота'

    def handle(self, *args, **kwargs):
        main()