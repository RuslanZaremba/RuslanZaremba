import random

# def result(a, b):
#     """
#     Вункция семмирует a и b.
#     :param a: первое число
#     :type a: int
#     :param b: второе число
#     :type b: int
#     :return: sum numbers
#     :rtype: int
#     """
#     return a - b
# print(result(2, 6))

# def myfunc(a, b, c='/', d):
#     """
#      :param a: number
#     :type: int
#     :param b: number
#     :type: int
#     :param c: string
#     :type: str
#     :return: int
#     """
#     if d is False:
#         a, b = b, a
#     if c == '-':
#         return a - b
#     elif c == '+':
#         return a + b
#     elif c == '*':
#         return a * b
#     else:
#         if b != 0:
#             return a / b
#
#
# print(myfunc(2, 3, '-', True))


s = [
    [1, 2, 8],
    [4, 12, 6],
    [7, 8, 8]
]


# def max(a, num_stolb):
#     num_stolb -= 1
#     max_element = 0
#     if num_stolb <= len(a[0]):
#         for i in a:
#             for j in range(len(i)):
#                 if j == num_stolb and max_element < i[j]:
#                     max_element = i[j]
#         return max_element
#     return 'Error'
# print(max(a, 3))

# def dina(matrix, num_elemett):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):     #ЗАЧЕМ ПРОХОДИТЬ ПО РАНЖУ,ЕСЛИ J ДАЕТ ЗНАЧЕНИЯ
#             if matrix[i][j] == num_elemett:
#                 matrix[i][j] = 0
#     return matrix

# print(dina(s, 8))
# matrix = dina(s, 8)

# for i in matrix:
#     for j in i:
#         print(j, end='\t')
#     print('\n')

# def dina(matrix):
#     a = 0
#     b = len(matrix[0]) - 1
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if j == a:
#                 matrix[i][j] = 1
#         if a != b:
#             matrix[i][b] = 0
#         a += 1
#         b -= 1
#     return matrix
# print(dina(s))

# def change_zero(matrix, average, max_element):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] < average:
#                 matrix[i][j] = 0
#     return matrix
#
#
# def change_one(matrix, average, max_element):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] > average and matrix[i][j] != max_element:
#                 matrix[i][j] = 1
#     return matrix
#
#
# def max_average(matrix):
#     average = 0
#     max_element = 0
#     for i in matrix:
#         for j in i:
#             average += j
#             if max_element < j:
#                 max_element = j
#     average = int(average / 9)
#     matrix = change_zero(matrix, average, max_element)
#     matrix = change_one(matrix, average, max_element)
#     return matrix


# def change(matrix):
#     a = 0
#     max_element = 0
#     for i in matrix:
#         for j in i:
#             if max_element < j:
#                 max_element = j
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if j == a and j != max_element:
#                 matrix[i][j] = random.randint(0, 10)
#                 a += 1
#     return matrix
# print(change(s))
#
#
# print(change(s))
# a = [
#     [1, 2, 8],
#     [4, 12, 6],
#     [7, 8, 8]
# ]
# b = [
#     [0, 6, 8],
#     [4, 13, 1],
#     [7, 9, 8]
# ]
#
# def change_after_diagonal(matrix_a, matrix_b):
#     pass
#
# def change_before_diagonal(matrix_a, matrix_b):
#     index = 0
#     for i in range(len(matrix_a)):
#         for j in range(len(matrix_a[i])):
#             if i == index + 1:
#                 matrix_a[i][j],
