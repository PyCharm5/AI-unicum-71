import json
from controller import register_user, login_user, is_valid_age
from model import load_menu, display_menu, choose_items
from view import price_print


if __name__ == "__main__":
    action = input("Введите 'register' для регистрации или 'login' для входа: ").strip().lower()
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    menu = open('menu.json', 'r')
    users = open('users.json', 'r')


    if action == 'register':
        age = input("Введите возраст: ")
        while not is_valid_age(age):
            print("Возраст должен быть положительным целым числом. Попробуйте снова.")
            age = input("Введите возраст: ")
        register_user(username, password, int(age))
    elif action == 'login':
        login_user(username, password)
    else:
        print("Неверное действие.")

    menu = load_menu('menu.json')
    with open('users.json', 'r') as file:
        user_data = json.load(file)
    # Запрос возраста у пользователя
    age = user_data[username]['age']

    # Отображение меню
    display_menu(menu)

    # Выбор позиций из меню
    total_price = choose_items(menu, age)

    price_print(total_price)