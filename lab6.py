import telebot
import requests

bot = telebot.TeleBot('5906607966:AAGpG3keLCGM-ZF6XblUQHHGeFGV5NKC_xg')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Доброго времени суток!  Напиши /help, ')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Чтобы получить фото, напиши /photo')

@bot.message_handler(commands=['photo'])
def photo(message):
    r = requests.get('http://thecatapi.com/api/images/get?format=src')
    url = r.url
    bot.send_photo(message.chat.id, url)



@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id,"Приветики, напиши /help")
    else:
        bot.send_message(message.chat.id,"Напиши /help")



bot.polling(none_stop=True)