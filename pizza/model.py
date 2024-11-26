import json

log = open("log.txt", 'w', encoding='utf-8')
def load_menu(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# Функция для отображения меню
def display_menu(menu):
    print("Меню:")
    print("\nЕда:")
    for item in menu['food']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

    print("\nБезалкогольные напитки:")
    for item in menu['non_alcoholic_drinks']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

    print("\nАлкогольные напитки:")
    for item in menu['alcoholic_drinks']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")


# Функция для выбора позиций из меню
def choose_items(menu, age):
    total_price = 0
    while True:
        item_name = input("\nВведите название позиции для заказа (или ' выход' для завершения): ").strip()

        if item_name.lower() == 'выход':
            break

        # Проверка на наличие позиции в меню
        found = False
        for category in ['food', 'non_alcoholic_drinks', 'alcoholic_drinks']:
            for item in menu[category]:
                if item['name'].lower() == item_name.lower():
                    found = True
                    if category == 'alcoholic_drinks' and age < 18:
                        print("Вы не можете заказать алкогольные напитки, так как вам нет 18 лет.")
                    else:
                        total_price += item['price']
                        print(f"Вы добавили {item['name']} к заказу.")
                        log.write(f'{item["name"]} - добавлено в корзину')
                    break
            if found:
                break

        if not found:
            print("Эта позиция не найдена в меню. Попробуйте снова.")

    return total_price
