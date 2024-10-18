numb = int(input())
lst_numb = 1
result = ""

def count(numb, lst_numb):
    global result
    if lst_numb > numb:
        result = "NO"
    else:
        if lst_numb == numb:
            result = "YES"
        else:
            lst_numb *= 2
            count(numb, lst_numb)

count(numb, lst_numb)
print(result)
