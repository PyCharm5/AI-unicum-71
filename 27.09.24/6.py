try:
    numb = float(input())
except:
    print("Введите число")
    exit()

if numb > 20:
    print("Больше 20")
elif numb < 10:
    print("Меньше 10")
else:
    print("Между 10 и 20")