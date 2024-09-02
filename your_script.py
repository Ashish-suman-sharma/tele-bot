from flask import Flask
import telebot
from telebot import types

app = Flask(__name__)

# Your bot token
TOKEN = "7306962151:AAGU0Rm_agYfLCSXScptj_UZaQgBcseiG8Q"
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

# Set webhook
def set_webhook():
    webhook_url = "https://your-render-url.onrender.com/webhook"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    set_webhook()
    app.run(host='0.0.0.0', port=80)
