import random
import json


def saver(matrix, file):
    with open(file, 'w') as file:
        data = {'matrix': matrix}
        file.write(json.dumps(data))


matrix = [[random.randint(1, 10) for i in range(0, 5)] for j in range(0, 5)]

saver(matrix, 'text_files/matrix.json')

with open('text_files/matrix.json') as file:
    matrix_unpacked = json.loads(file.read())['matrix']
for i in range(len(matrix_unpacked)):
    for j in range(len(matrix_unpacked[i])):
        if matrix_unpacked[i][j] % 2 == 0:
            matrix_unpacked[i][j] = 0
saver(matrix_unpacked, 'text_files/new_matrix.json')


# def saver(matrix, file):
#     with open(file, 'w') as f:
#         data = {'matrix': matrix}
#         f.writelines(json.dumps(data))
#
#
# matrix = [[random.randint(1, 10) for i in range(0, 5)] for j in range(0, 5)]
#
# saver(matrix, 'matrix.json')
#
# with open('matrix.json', 'r') as f:
#     matrix = json.loads(f.readline())['matrix']
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0:
#             matrix[i][j] = 0
#
# saver(matrix, 'matrix.json')

