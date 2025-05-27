# from django.apps import AppConfig


# class TelegramBotConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'telegram_bot'

#     def ready(self):
#         from . import bot  # Запускаем бота при старте приложения

# telegram_bot/apps.py
from django.apps import AppConfig

class TelegramBotConfig(AppConfig):
    name = 'telegram_bot'

    def ready(self):
        # Не обязательно импорровать bot здесь, если вы используете команду управления
        pass        