import telebot
import os

TOKEN = os.getenv("8917402104:AAGJ7IXwK1x6PFPi3tjEUzCUkb4NWKbGQ7E")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салом! Ман дар Render 24/7 кор мекунам 🔥")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Ту гуфтӣ: {message.text}")

print("Bot started...")
bot.polling()
