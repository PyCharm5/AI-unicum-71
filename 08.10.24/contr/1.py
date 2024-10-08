mass = input().split(" ")
mass = [int(x) for x in mass]
summ = 0

for el in mass:
    if el > 0:
        summ += el

print(summ)