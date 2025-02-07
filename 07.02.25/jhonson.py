import time
lst = [1, 2, 3]
lst_all_iter = []
lst_copy = lst.copy()
going = [-1, -1, -1]

i = 0

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
def iter(lst):
    while lst[::-1] != lst_copy:
        for i in range(len(lst))[::-1]:
            if (lst[i] > lst[i + going[i]]) and i != 0:
                lst[i], lst[i + going[i]] = lst[i + going[i]], lst[i]
                lst_all_iter.append(lst.copy())
                print(lst)
            else:
                going[i] *= -1

    while lst != lst_copy:
        for i in range(len(lst)):
            if (lst[i] < lst[i + going[i]]) and i != 0:
                lst[i], lst[i + going[i]] = lst[i + going[i]], lst[i]
                lst_all_iter.append(lst.copy())
                print(lst)
            else:
                going[i] *= -1

iter(lst)