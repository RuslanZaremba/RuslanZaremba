import random
import json
import pprint
# matrix = [[random.randint(1, 10) for i in range(0, 5)] for j in range(0, 5)]
# with open('text_files/matrix.json', 'w') as file:
#     file.write(json.dumps(matrix))
# with open('text_files/matrix.json', 'r') as file:
#     with open('text_files/new_matrix.json', 'w') as new_file:
#         my_matrix = json.loads(file.read())
#         for i in range(len(my_matrix)):
#             for j in range(len(my_matrix[i])):
#                 if my_matrix[i][j] % 2 == 0:
#                     my_matrix[i][j] = 0
#         new_file.write(json.dumps(my_matrix))

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

data = {}
with open('big_data.json', 'r', encoding="UTF-8") as file:
    data = json.loads(file.read())
    pprint.pprint(data)
    print(data)


with open('big_data.json', 'w', encoding="UTF-8") as file:
    data = json.loads(file.read())