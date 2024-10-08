try:
    numb = int(input("Введите число:   ")) #Ввод числа для поиска
    start = int(input("Введите начало:   ")) #Ввод начала поиска
    finish = int(input("Введите конец:   ")) #Ввод конца поиска
except:
    print("Введите число")
    exit()

print(numb in range(start, finish + 1)) #Проверка нахождения числа в промежутке

if (numb >= start) and (numb <= finish): print(True)
else: print(False)
