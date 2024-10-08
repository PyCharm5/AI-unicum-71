import random #Импорт библиотеки
numb = int(input("Введите кол-во чисел:   ")) #Ввод длины списка

matrix = [random.randint(1,15)for i in range(numb)] #Создание случайного списка длины numb
print(matrix) #Вывод списка
print(max(matrix)) #Вывод максимального числа в списке
print(min(matrix)) #Вывод минимального числа в списке
