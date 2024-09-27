try:
    f_numb = float(input())
    s_numb = float(input())
    t_numb = float(input())
except:
    print("Введите число")
    exit()

if (f_numb > s_numb) and (f_numb > t_numb):
    print(f_numb)
elif (s_numb > f_numb) and (s_numb > t_numb):
    print(s_numb)
else:
    print(t_numb)