import json

log = open("log.txt", 'w', encoding='utf-8')
rest_menu = open('menu.json', 'r')
chek = open('chek.txt', 'w')

def is_valid_age(age):
    return age.isdigit() and int(age) > 0


# Функция для регистрации пользователя
def register_user(username, password, age):
    user_data = {}

    # Проверка, существует ли пользователь
    if username in user_data:
        print("Пользователь уже существует.")
        return False

    # Добавление нового пользователя
    user_data[username] = {
        "password": password,
        "age": age
    }

    # Сохранение данных в JSON файл
    with open('users.json', 'w') as file:
        json.dump(user_data, file)

    log.write(f'{user_data[username]} - регистрация\n')
    print("Пользователь зарегистрирован.")
    return True


# Функция для входа пользователя
def login_user(username, password):


    with open('users.json', 'r') as file:
        user_data = json.load(file)

    # Проверка данных пользователя
    if username in user_data and user_data[username]["password"] == password:
        print("Вход выполнен успешно.")
        log.write(f'{user_data[username]} - вход\n')
        print(f"Возраст пользователя: {user_data[username]['age']}")
        return True
    else:
        print("Неверное имя пользователя или пароль.")
        return False

def do_chek(mass, schet, enter):
    print(mass)
    mass.append("="*30)
    mass.append("Ваш чек:")
    mass = mass[2:]
    for eat in set(mass):
        mass.append(f"{eat}: {None} руб. Х {mass.count(eat)} шт.")
    mass.append(f"Итого к оплате: {schet} руб.")
    mass.append(f"Внесено: {enter} руб.")
    mass.append(f"Сдача: {enter - schet} руб.")
    mass.append("=" * 30)
    print(mass)
    return mass


