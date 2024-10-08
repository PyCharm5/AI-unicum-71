import random
import datetime

enter_numb = 0
matrix = [random.randint(1,15)for i in range(10)]
matrix = sorted(list(set(matrix)))
secret_numb = random.choice(matrix)
cot, start = 0, datetime.datetime.now()

print(matrix)

while True:
    enter_numb = int(input("Введите число:   "))
    cot += 1
    if enter_numb == secret_numb:
        finish = datetime.datetime.now()
        print(f'\nЧисло найдено за {cot} попыток.')
        print(f'Это заняло {datetime.datetime.now() - start}.')
        exit()
    elif enter_numb > secret_numb:
        print("Число меньше")
        matrix = matrix[:matrix.index(enter_numb)]
        print(matrix)
    else:
        print("Число больше")
        matrix = matrix[matrix.index(enter_numb)+1:]
        print(matrix)
    # if input("Продолжить? Да/Нет:   ") == "Да":
    #     continue
    # else:
    #     print(f'Загаданное число было {secret_numb}')
    #     exit()