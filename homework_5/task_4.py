import random


def matrix(n):
    data = []
    for i in range(0, n):
        stroka = []
        for j in range(0, n):
            stroka.append(random.randrange(1, 100))
        data.append(stroka)
    return data


matrix1 = matrix(4)
matrix2 = matrix(4)
ma = matrix1 + matrix2
print(matrix1)
print(matrix2)


def sum_matrix(a, b):
    sum_matrix = []
    for i in range(len(a)):
        sum_str = []
        for j in range(len(a[i])):
            sum_str.append(a[i][j] + b[i][j])
        sum_matrix.append(sum_str)
    return sum_matrix


print(sum_matrix(matrix1, matrix2))
