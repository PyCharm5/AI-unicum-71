import time
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
def johnson_trotter(n):
    # Инициализация
    perm = list(range(n))  # Начальная перестановка
    dir = [1] * n  # Направления (1 - вправо, -1 - влево)
    result = []

    def print_permutation():
        result.append(perm[:])  # Сохраняем текущую перестановку

    def get_largest_mobile():
        largest_mobile = -1
        largest_mobile_index = -1
        for i in range(n):
            if dir[i] == 1 and i < n - 1 and perm[i] > perm[i + 1]:  # Вправо
                if perm[i] > largest_mobile:
                    largest_mobile = perm[i]
                    largest_mobile_index = i
            elif dir[i] == -1 and i > 0 and perm[i] > perm[i - 1]:  # Влево
                if perm[i] > largest_mobile:
                    largest_mobile = perm[i]
                    largest_mobile_index = i
        return largest_mobile_index

    print_permutation()  # Сохраняем первую перестановку

    while True:
        mobile_index = get_largest_mobile()
        if mobile_index == -1:
            break  # Все перестановки сгенерированы

        # Меняем местами мобильный элемент с соседом
        swap_index = mobile_index + dir[mobile_index]
        perm[mobile_index], perm[swap_index] = perm[swap_index], perm[mobile_index]

        # Меняем направление для всех элементов, больших мобильного
        for i in range(n):
            if perm[i] > perm[swap_index]:
                dir[i] = -dir[i]

        print_permutation()  # Сохраняем текущую перестановку

    return result

# Пример использования
n = 10**6
permutations = johnson_trotter(n)