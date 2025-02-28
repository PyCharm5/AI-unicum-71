num1 = int(input())
num2 = int(input())
num3 = int(input())

lst = [num1, num2, num3]

for first_id in range(3):
    for second_id in range(first_id, 3):
        print(lst[first_id], lst[second_id])