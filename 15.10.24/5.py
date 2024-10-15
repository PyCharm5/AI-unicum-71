import math

x1 = int(input())
corn_b = int(input())
corn_c = int(input())
corn_a = 180 - corn_b - corn_c
sin_a, sin_b, sin_c = 0, 0, 0

def count():
    sin_a = math.sin(math.radians(corn_a))
    sin_b = math.sin(math.radians(corn_b))
    sin_c = math.sin(math.radians(corn_c))

    x2 = x1*sin_b/sin_c
    x3 = x1*sin_a/sin_c
    return x2, x3
print(count())