import telebot
import random
import string
import threading

API_TOKEN = '7882467666:AAFmco2CZx3Kd5WrOtYskoUmAwlitQ8KnAw'
CHAT_ID = '-1002302953669'

bot = telebot.TeleBot(API_TOKEN)

def generate_random_string_with_emojis(length=100):
    # Определяем набор символов: буквы, цифры, эмодзи и специальные символы
    letters = string.ascii_letters  # Буквы (строчные и заглавные)
    digits = string.digits  # Цифры
    # Расширенный набор эмодзи
    emojis = [
        '😀', '😂', '🥺', '😍', '😎', '🤖', '🎉', '🚀', '🌟', '💖',
        '🍀', '🌈', '🔥', '✨', '💡', '🎈', '🎶', '🌻', '🍕', '🍣',
        '🍩', '🍉', '🍓', '🍪', '🍦', '🍰', '🍫', '🍭', '🍬', '🍿'
    ]
    # Расширенный набор специальных символов
    special_chars = string.punctuation + "•★☆♠♣♥♦♪♫☀☁☂☃✈✉✌✍✏✒✖➕➖➗➤➥"

    # Объединяем все символы в один набор
    characters = letters + digits + ''.join(emojis) + special_chars

    # Генерируем случайную строку
    random_string = ''.join(random.choice(characters) for _ in range(length))

    # Выводим все специальные символы
   # print("Все специальные символы:", special_chars)

    return random_string

def send_message():
    spam_text = generate_random_string_with_emojis(length=100)  #
    bot.send_message(CHAT_ID, spam_text)
    threading.Timer(5, send_message).start()  # Запускаем функцию снова через 1 секунду


# Запускаем отправку сообщений
send_message()

# Запускаем бота
bot.polling(none_stop=True)