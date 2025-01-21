"""Уровень С Сложный"""
import random
import psutil

print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")

n = int(input())
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]

def print_matrix(matrix):
    for row in matrix:
        row = map(str, row)
        print(" ".join(row))
    print("\n")

print_matrix(matrix)

matrix.insert(0, matrix[-1])
del matrix[-1]

print_matrix(matrix)
