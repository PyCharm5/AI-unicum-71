"""Уровень С Сложный"""
import random

n = int(input())
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]

def sort_row(row): #Сортировка вставкой
    for i in range(1, len(row)):
        el = row[i]
        i2 = i - 1
        while i2 >= 0 and row[i2] > el:
            row[i2 + 1] = row[i2]
            i2 -= 1
            row[i2 + 1] = el

def tranpon(matrix):
    result = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        result.append(row)

    return result

def print_matrix(matrix):
    for row in matrix:
        row = map(str, row)
        print(" ".join(row))
    print("\n")

print_matrix(matrix)

matrix = tranpon(matrix).copy()
for row in matrix:
    sort_row(row)
matrix = tranpon(matrix).copy()

print_matrix(matrix)