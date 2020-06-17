import random
import json

matrix = [[random.randint(1, 10) for i in range(5)] for j in range(5)]
with open('text_files/matrix.json', 'w') as file:
    file.write(json.dumps(matrix))
with open('text_files/matrix.json', 'r') as file:
    with open('text_files/new_matrix.json', 'w') as new_file:
        my_matrix = json.loads(file.read())
        for i in range(len(my_matrix)):
            for j in range(len(my_matrix[i])):
                if my_matrix[i][j] % 2 == 0:
                    my_matrix[i][j] = 0
        new_file.write(json.dumps(my_matrix))



