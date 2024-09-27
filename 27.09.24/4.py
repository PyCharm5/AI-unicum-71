try:
    f_numb = float(input())
    s_numb = float(input())
except:
    print("Введите число")
    exit()

if (f_numb > 10) and (s_numb > 10):
    print(True)
else:
    print(False)