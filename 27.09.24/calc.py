defc = input("Введите действие(+, - , * , /): ")
result = 0

try:
    f_numb = float(input("Введите 1 число: "))
    s_numb = float(input("Введите 2 число: "))
except:
    print("Введите число")
    exit()

def plus(f_numb, s_numb):
    return f_numb + s_numb

def minus(f_numb, s_numb):
    return f_numb - s_numb

def multi(f_numb, s_numb):
    return f_numb * s_numb

def divide(f_numb, s_numb):
    return f_numb / s_numb

def printf(f_numb, s_numb, defc, result):
    print(f'{f_numb} {defc} {s_numb} = {result}')

if defc == "+":
    plus(f_numb, s_numb)
    printf(f_numb, s_numb, defc, plus(f_numb, s_numb))
elif defc == "-":
    minus(f_numb, s_numb)
    printf(f_numb, s_numb, defc, minus(f_numb, s_numb))
elif defc == "*":
    multi(f_numb, s_numb)
    printf(f_numb, s_numb, defc, multi(f_numb, s_numb))
else:
    divide(f_numb, s_numb)
    printf(f_numb, s_numb, defc, divide(f_numb, s_numb))
