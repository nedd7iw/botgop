import telebot
import re

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def handler_text(message):

    if re.search(r'\bванплас\b', message.text):
        bot.reply_to(message, "за ванплас и двор стреляю в упор")

    elif re.search(r"\bсамсунг\b", message.text):
        bot.reply_to(message, "фууу, этим еще кто-то пользуется?")

    elif re.search(r"\bсони\b", message.text):
        bot.reply_to(message, "они и то лучше самсунга")

    elif re.search(r"\bмейзу\b", message.text):
        bot.reply_to(message, "пойдет, но ванплас лучше")


bot.polling()
