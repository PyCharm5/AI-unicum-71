import random #Импорт библиотеки
numb = int(input("Введите кол-во чисел:   ")) #Ввод длины списка

matrix = [random.randint(1,15)for i in range(numb)] #Создание случайного списка длины numb
print(matrix) #Вывод списка
minN = 0
maxN = 16

for el in matrix: #Перебор элементов списка
    if el < maxN:
        maxN = el 
    if el > minN:
        minN = el

print(maxN)
print(minN)
