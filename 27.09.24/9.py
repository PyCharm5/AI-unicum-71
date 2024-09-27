try:
    numb = float(input())
except:
    print("Введите число")
    exit()

if (numb % 4 == 0) and (numb % 100 != 0) or (numb % 400 == 0):
    print(True)
else:
    print(False)