import math
schet = 0
chek = []
file = open('chek.txt', 'r+')

rest_menu = {
    "Салат" : 123,
    "Суп" : 150,
    "Курица" : 250,
    "Пельмени" : 250,
    "Много пельменей" : 450,
    "Хлеб" : 30,
    "Говядина" : 400,
    "Пирог" : 250,
    "Круглый пирог" : 350
}
mass = list(map(str, input().split()))
enter = int(input('Сколько внесено:  '))

def summ(mass, schet):
    for eat in mass:
        schet += rest_menu.get(eat)
    return schet

def do_chek(mass, schet):
    chek.append("="*30)
    chek.append("Ваш чек:")
    for eat in set(mass):
        chek.append(f"{eat}: {rest_menu.get(eat)} руб. Х {mass.count(eat)} шт.")
    chek.append("")
    chek.append(f"Итого к оплате: {summ(mass, schet)} руб.")
    chek.append(f"Внесено: {enter} руб.")
    chek.append(f"Сдача: {enter - summ(mass, schet)} руб.")
    chek.append("=" * 30)

def printf():
    summ(mass, schet)
    do_chek(mass, schet)
    for el in chek:
        file.writelines(el)
        file.writelines("\n")
        print(el)

printf()