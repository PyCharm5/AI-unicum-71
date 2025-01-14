import telebot

# Укажите токен вашего бота
TOKEN = '8071487784:AAG9lYZLqQpad4_LM-5YraH3IZWkNp3VcoE'  # Замените на ваш токен
bot = telebot.TeleBot(TOKEN)
dct = {}

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    dct[message.message_id] = message.text
    try:
        for i in range(1, 200):
            if message.text.count(chr(i)) > 5:
                bot.delete_message(message.chat.id, message.message_id)
                print("Сообщение удалено: ", message.text)
        if dct[message.message_id] == dct[message.message_id - 1]:
            bot.delete_message(message.chat.id, message.message_id)

            print("Сообщение удалено: ", message.text)
        # Проверяем условия для удаления сообщения
        if (message.from_user.username and message.from_user.username.endswith('bot')) or \
           ('VENOM' in message.text) or \
           ('venom' in message.text) or \
           ('мени с ' in message.text) or \
           (len(message.text) < 3) or \
           (len(message.text) > 50):
            bot.delete_message(message.chat.id, message.message_id)
            print("Сообщение удалено: ", message.text)

    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

# Запускаем бота
if __name__ == '__main__':
    bot.polling(none_stop=True)