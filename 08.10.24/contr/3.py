import random
numb = int(input("Введите кол-во чисел:   "))

matrix = [random.randint(1,15)for i in range(numb)]
print(matrix)
print(max(matrix))
print(min(matrix))