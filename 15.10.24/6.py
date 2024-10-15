x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

def count(x1, x2):
    return max(x1, x2)


print(count(count(x1, x2), count(x3, x4)))