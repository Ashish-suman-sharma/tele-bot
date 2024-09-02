# -*- coding: utf-8 -*-
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check if the package is installed and install it if not
try:
    import telebot
except ImportError:
    install("pyTelegramBotAPI")
    import telebot  # Try importing again after installation

from telebot import types
from telebot.apihelper import ApiTelegramException

# Your bot token (be sure to keep this secret!)
TOKEN = "7521429771:AAF9RCwrDosdPeBuyeLIsbjdAKbglOZ0dfo"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://google-clone-rust-nine.vercel.app/")
    button = types.InlineKeyboardButton("Earn Now", web_app=web_app)
    markup.add(button)
    bot.send_message(message.chat.id, 
        "🎉 Welcome to Pepe Layer 2! 🎉\n\n"
        "💰 Start mining coins now! Tap the big logo to collect coins and complete tasks to earn more.\n\n"
        "🔗 Refer & Earn: Share your referral link and earn rewards when friends join!\n\n"
        "✨ Explore:\n\n"
        "• Home: Track your progress\n"
        "• Tasks: Earn extra coins\n"
        "• Refer & Earn: Share and earn", 
        reply_markup=markup)

try:
    bot.polling()
except ApiTelegramException as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
