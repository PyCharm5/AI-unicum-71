try:
    numb = float(input())
except:
    print("Введите число")
    exit()

if numb in range(10, 21):
    print(True)
else:
    print(False)