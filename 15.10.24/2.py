x = int(input())

def count():
    if x >= 2:
        return x*x + 4*x + 5
    elif x < -2:
        return x*x
    else:
        return 4

print(count())