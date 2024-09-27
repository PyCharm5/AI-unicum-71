try:
    numb = float(input())
except:
    print("Введите число")
    exit()

if numb % 2 == 0:
    print(True)
else:
    print(False)