fib_mass = [1, 1]

def count(fib_mass):
    if len(fib_mass) > 100:
        print(fib_mass)
    else:
        fib_summ = fib_mass[len(fib_mass)-1] + fib_mass[len(fib_mass)-2]
        fib_mass.append(fib_summ)
        count(fib_mass)

count(fib_mass)
