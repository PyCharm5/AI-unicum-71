mass = input().split(" ") #Ввод списка
mass = [int(x) for x in mass] #Перевод значений в числа
summ = 0

for el in mass: #Перебор элементов
    if el > 0: #Проверка на положительность
        summ += el #Прибавление

print(summ) #Вывод суммы
