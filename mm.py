import requests
from bs4 import BeautifulSoup
from telebot import types
import telebot
bot = telebot.TeleBot("6476334435:AAGREDmaK55EpFxCck53DDm0bqQglN44pJs")
@bot.message_handler(commands=["start"])
def starlt(message):
    btn1 = types.InlineKeyboardMarkup(row_width=1)
    pro = types.InlineKeyboardButton(text ="چنلمه اگه عشقت کشید دنبال کن",url = "https://t.me/freeconfingv2rayngm")
    btn1.add(pro)
    bot.send_message(message.chat.id ,"سلام دلقک اسمتو به انگلیسی وارد کن برات قشنگش کنم",reply_markup=btn1)
@bot.message_handler(func =lambda message :True)
def ren(message):
    nn = message.text
    url = "https://coolnames.online/cool.php"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Content-Length": "24",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "PHPSESSID=ga8f9usm0m4qfrtcjp167ktvs3",
        "Origin": "https://coolnames.online",
        "Pragma": "no-cache",
        "Referer": "https://coolnames.online/English-decoration",
        "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Platform": "\"Android\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "name": f"{nn}",
        "get": "english"
    }
    req = requests.post(url ,headers=headers ,data=data).text
    soup = BeautifulSoup(req, 'html.parser')
    all = soup.find_all('textarea')
    for name in all:
        word = name.text
        bot.send_message(message.chat.id ,word)
    bot.send_message(message.chat.id ,"تموم شد حالا بحی بده")
bot.polling()
