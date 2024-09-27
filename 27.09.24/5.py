try:
    numb = float(input())
except:
    print("Введите число")
    exit()

if numb > 0:
    print("+")
elif numb < 0:
    print("-")
else:
    print("0")