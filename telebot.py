import telebot
from telebot import types

bot = telebot.TeleBot("7306962151:AAGU0Rm_agYfLCSXScptj_UZaQgBcseiG8Q")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo("https://ashishsuman.me/pepe-backup/")
    button = types.InlineKeyboardButton("Search and Earn", web_app=web_app)
    markup.add(button)
    bot.send_message(message.chat.id, 
        "🎉 Welcome to Search and earn 🎉\n\n"
        "🔍 Start searching content on the internet and earn money while you do! Tap the button below to begin.\n\n"
        "💸 Earn by watching videos and refer friends to increase your earnings.\n\n"
        "✨ Explore:\n\n"
        "• Home: Track your progress\n"
        "• Search & Earn: Find content and make money\n"
        "• Refer & Earn: Share your link and earn rewards when friends join!", 
        reply_markup=markup)

bot.polling()
