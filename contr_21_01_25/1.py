"""Уровень С Сложный"""
import random
import time
import psutil

print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

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
def p_sort(lst):

    for n in range(len(lst) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break

    return lst

@time_measuring
def s_sort(lst):

    lst.sort()

    return lst

p_sort(lst=lst.copy())
s_sort(lst=lst.copy())

"""
Итого:
Пузырьковая сортирока - ~8.026535749435425 сек на 10000 элементов
.sort() - ~0.0009975433349609375 сек на 10000 элементов
"""
