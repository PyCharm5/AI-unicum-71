x1_1 = int(input())
x2_1 = int(input())
x3_1 = int(input())
y1_1 = int(input())
y2_1 = int(input())
y3_1 = int(input())

x1_2 = int(input())
x2_2 = int(input())
x3_2 = int(input())
y1_2 = int(input())
y2_2 = int(input())
y3_2 = int(input())


def count(x1, x2, x3, y1, y2, y3):
    return 0.5*abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))

s1 = count(x1_1, x2_1, x3_1, y1_1, y2_1, y3_1)
s2 = count(x1_2, x2_2, x3_2, y1_2, y2_2, y3_2)

if s1>s2:
    print(1)
else:
    print(2)