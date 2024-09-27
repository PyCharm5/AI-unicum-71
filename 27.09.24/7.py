try:
    f_numb = float(input())
    s_numb = float(input())
    t_numb = float(input())
except:
    print("Введите число")
    exit()

if (f_numb % 2 == 0) or (s_numb % 2 == 0) or (t_numb % 2 == 0):
    print(True)
else:
    print(False)