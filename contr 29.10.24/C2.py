def length():
    mass = list(map(int, input().split(" ")))  # ввод координат стороны - х1 и у1, х2 и у2
    x = abs(mass[0] - mass[2])  # расстояние между точками по х
    y = abs(mass[1] - mass[3])
    return (x*x + y*y) ** 0.5  # рассотяние между точками по т. Пифагора

def per_triang():
    a = length()  # вычисление длины каждой стороны
    print(a)  # вывод пользователю значения каждой стороны
    b = length()
    print(b)
    c = length()
    print(c)
    p = (a+b+c)/2   # нахождение полупериметра

    return (p*(p-a)*(p-b)*(p-c)) ** 0.5  # нахождение площади по формуле Герона

print(per_triang())