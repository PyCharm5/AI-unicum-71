import telebot
import time

API_TOKEN = '7537542023:AAGMEpNEDBf0ThJkczmt0PlSjh8tYSqaqPw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Выберите тип ввода: текст или файл')
    bot.register_next_step_handler(message, handle_input_type)

def handle_input_type(message):
    type_input = message.text.strip().lower()
    if type_input == "текст":
        get_numb(message)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте файл с числами через пробел.')
        bot.register_next_step_handler(message, get_document)

def get_numb(message):
    bot.send_message(message.chat.id, 'Отправьте числа через пробел')
    bot.register_next_step_handler(message, process_numbers)

def process_numbers(message):
    try:
        numbs = list(map(int, message.text.split(" ")))
        start = time.perf_counter()
        sorted_numbers = sorted(numbs)
        end = time.perf_counter()

        bot.send_message(message.chat.id, ' '.join(map(str, sorted_numbers)))
        bot.send_message(message.chat.id, f'Сортировка заняла {(end - start) * 1000} секунд.')
    except:
        bot.send_message(message.chat.id, 'Ошибка: убедитесь, что вы вводите только числа.')

# Функция для обработки файла с числами
def get_document(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('numbers.txt', 'wb') as new_file:
        new_file.write(downloaded_file)

    with open('numbers.txt', 'r') as f:
        numbers = list(map(int, f.read().strip().split()))

    start = time.perf_counter()
    sorted_numbers = sorted(numbers)
    end = time.perf_counter()

    with open('sorted_numbers.txt', 'w') as f:
        f.write(' '.join(map(str, sorted_numbers)))

    with open('sorted_numbers.txt', 'rb') as f:
        bot.send_document(message.chat.id, f)

    bot.send_message(message.chat.id, f'Сортировка заняла {(end - start) * 1000} секунд.')

def main():
    bot.polling(none_stop=True)

main()