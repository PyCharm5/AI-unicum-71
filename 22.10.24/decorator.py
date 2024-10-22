mass = []
numb = 0

def double_result(func):
    def wrapper():
        mass = list(map(int, input().split()))
        return func(mass, numb)
    return wrapper

@double_result
def double_all(mass, numb):
    if numb >= len(mass):
        return mass
    else:
        mass[numb] = mass[numb]*2
        numb += 1
        double_all(mass, numb)

double_all()