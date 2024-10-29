mass = list(map(int, input().split(" "))) # ввод элементов через пробел

def x2():
    global mass, summ
    new_list = list(filter(lambda el: (el%2 == 1), mass))  # выбрана для сокращения кода
    print(sum(new_list), "Сумма неч. чисел")  # сумма чисел в списке нечетных чисел
    print(", ".join(str(i) for i in new_list), "Список неч. чисел")  # объединение чисел спика для красивого вывода

x2()