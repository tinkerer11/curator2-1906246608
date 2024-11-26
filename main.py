from telebot import TeleBot

bot = TeleBot('7776399663:AAFwV4fF1YOB4cLJ2BnLo_fu-ZGRY7e2w1A')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я сигма, я и сделаю из тебя сигму')


@bot.message_handler(commands=['Кто_такой_сигма?'])
def sigma(message):
    bot.send_message(message.chat.id,
                     'термин из интернет-сленга, которым называют мужчин-одиночек и независимых от общества личностей')


@bot.message_handler(commands=['я_сигма!'])
def nice(message):
    bot.send_message(message.chat.id, 'Молодец, так держать')


@bot.message_handler(commands=['Эх... Я не сигма'])
def nice_1(message):
    bot.send_message(message.chat.id, 'Тогда жди моих указаний')


bot.infinity_polling()