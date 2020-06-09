import math
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
print(ma)


def sum_matrix(a, b):
    pass


m = [1, 1, 1]
b = [12, 15, 18]
c = []

for i in range(len(m)):
    for j in range(len(b)):
        x = m[i] + b[j]
        c.append(x)
print(c)


