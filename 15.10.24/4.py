import math

x1 = int(input())
x2 = int(input())

def count():
    return math.gcd(x1, x2)

print(count())