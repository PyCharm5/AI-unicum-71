n = int(input())
mass = []
lst_numb = 1

def count(n, lst_numb):
    if lst_numb > n:
        return 0
    else:
        mass.append(lst_numb)
        lst_numb += 1
        count(n, lst_numb)

count(n, lst_numb)
print(mass)
