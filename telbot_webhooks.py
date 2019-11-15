
from flask import Flask, request
# импортируем модуль телеграмбот из библиотеки pyTelegramBotAPI
import telebot
# импортируем основные настройки проекта
from settings import config
# импортируем все обработчки бота
from handlers.handler_main import HandlerMain
import time

API_TOKEN = config.TOKEN
bot = telebot.TeleBot(API_TOKEN, threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="URL".format(API_TOKEN))

app = Flask(__name__)


@app.route('/{}'.format(API_TOKEN), methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


handler = HandlerMain(bot)

handler.handle()

if __name__ == '__main__':
    app.run()

