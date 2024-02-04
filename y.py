import requests
import os
import telebot
token = ("6979355959:AAGnOiP-EOkfzNjx2nrQdlm9m43v5LOMdVk")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"Hello\n Wellcome To instagram Download Bot : video and Reels and photo  and Tv :  \nSend Link  Now ðŸ“Žâœ… \nCH  : @Abfullah_Abd_alsalam")
@bot.message_handler(func=lambda m:True)
def send(message):
    bot.send_message(message.chat.id,f"Wait Please",parse_mode="html") 
    bot.send_video("-1001903749072",f"{message.text}",caption="Done âœ…ðŸ’— << @Abdullah_Abd_alsalam >> ")
bot.polling()
