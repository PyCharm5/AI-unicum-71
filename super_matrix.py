type = input()
n = int(input("Введите длину матрицы:  "))

matrix1, matrix2 = [], []
def summ(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result

def div(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)

    return result

def super(matrix1, n):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] * n)
        result.append(row)

    return result

def tranpon(matrix1):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[j][i])
        result.append(row)

    return result

def matrix_enter(n):
    matrix = []
    print(f"Введите элементы квадратной матрицы:")
    for i in range(n):
        while True:
            row = list(map(int, input(f"Строка {i + 1}: ").split()))
            matrix.append(row)
            break
    return matrix

def matrix_print(matrix1):
    for row in matrix1:
        print(" ".join(f"{elem}" for elem in row))

if type == "sum":
    matrix1 = matrix_enter(n)
    matrix2 = matrix_enter(n)
    matrix_print(summ(matrix1, matrix2))
elif type == "div":
    matrix1 = matrix_enter(n)
    matrix2 = matrix_enter(n)
    matrix_print(div(matrix1, matrix2))
elif type == "super":
    matrix1 = matrix_enter(n)
    n = int(input("Введите число:  "))
    matrix_print(super(matrix1, n))
else:
    matrix1 = matrix_enter(n)
    matrix_print(tranpon(matrix1))