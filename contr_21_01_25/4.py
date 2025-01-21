"""Уровень С Сложный"""
import random
import time

lst = [random.randint(1, 1000) for _ in range(10000)]
start_time = time.time()
end_time = time.time()
elapsed_time = end_time - start_time

def time_measuring(func):
    def wrapper(lst):
        start_time = time.time()
        res = func(lst)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        return res
    return wrapper

@time_measuring
def p_sort(lst): #Перебор

    max_el = 0
    for el in lst:
        if el > max_el:
            max_el = el

    print(max_el)
    return lst

@time_measuring
def s_sort(lst): #Пузырьковая

    for n in range(len(lst) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break

    print(lst[-1])
    return lst

p_sort(lst=lst.copy())
s_sort(lst=lst.copy())

"""
Итого:
Пузырьковая сортирока - 7.839069843292236 сек на 10**4 элементов
Перебор - 0.0009975433349609375 сек на 10**5 элементов
"""
