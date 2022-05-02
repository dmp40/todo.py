import telebot
token ='358196444:AAG9Fs2WB1uJVK0tnuBYmfsg4S48abZWero'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])

def echo(message):
    bot.send_message(message.chat.id, "Вы написали-" + message.text)
#постоянно обращается к серверу телеграм
bot.polling(none_stop=True)
