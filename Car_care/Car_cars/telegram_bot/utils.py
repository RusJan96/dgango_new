# telegram_bot/utils.py
import requests

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{YOUR_TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, data=payload)
    return response.json()