numb = int(input())
lst_numb = 1  #
result = ""

def count(numb, lst_numb):
    global result
    if lst_numb > numb:  # если число "проскочило" степень
        result = "NO"
    elif lst_numb == numb:  # если число совпало со степенью
        result = "YES"
    else:
        lst_numb *= 2  # след. степень двойки
        count(numb, lst_numb)  # рекурсия

count(numb, lst_numb)
print(result)