# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot("7521429771:AAF9RCwrDosdPeBuyeLIsbjdAKbglOZ0dfo")

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

bot.polling()

