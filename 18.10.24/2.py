a = int(input())
b = int(input())
mass = []
lst_numb = min(a, b)

def count(a, b, lst_numb):
    if lst_numb > max(a, b):
        return 0
    else:
        mass.append(lst_numb)
        lst_numb += 1
        count(a, b, lst_numb)

count(a, b, lst_numb)
print(mass)
