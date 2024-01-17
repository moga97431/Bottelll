from requests import get
from time import sleep
import telebot

  bot = telebot.TeleBot("6406574208:AAFzkKOHtAsFauTmhG8tsJcMK4Y1cd-X3jA")

m = get("https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/normal/vless").text

for t in m.split():
    if t.startswith("vless:"):
        bot.send_message(chat_id='-1001903749072', text=t)
    sleep(2)

      bot.polling()
