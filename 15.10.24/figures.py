import math

pi = math.pi
s, per, f_num, d1, d2, d3, h, rad = 0, 0, 0, 0, 0, 0, 0, 0

def enter():
    global f_num, d1, d2, d3, h, rad
    f_num = int(input("Введите номер фигуры:   "))
    if f_num == 1:
        print("Выбран прямоугольник")
        d1 = int(input("Введите первую сторону:   "))
        d2 = int(input("Введите вторую сторону:   "))
    elif f_num == 2:
        print("Выбран круг")
        rad = int(input("Введите радиус:   "))
    elif f_num == 3:
        print("Выбран треугольник")
        d1 = int(input("Введите первую сторону:   "))
        d2 = int(input("Введите вторую сторону:   "))
        d3 = int(input("Введите третью сторону:   "))
        h = int(input("Введите высоту:   "))
    else:
        print("Выбран ромб")
        d1 = int(input("Введите первую диагональ:   "))
        d2 = int(input("Введите вторую диагональ:   "))

def count():
    global f_num, d1, d2, d3, h, rad
    global s, per
    if f_num == 1:
        s = d1 * d2
        per = 2*d1 + 2*d2
    elif f_num == 2:
        s = pi * rad**2
        per = 2 * pi * rad
    elif f_num == 3:
        s = 0.5 * d1 * h
        per = d1 + d2 + d3
    else:
        s = (d1 * d2) / 2
        per = (((d1 / 2) ** 2) + ((d2 / 2) ** 2)) * 4

def printf():
    print(f'Площадь - {s}, периметр - {per}.')

enter()
count()
printf()