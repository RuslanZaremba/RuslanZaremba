# ЗАПИСЬ ФАЙЛА
li = [
    [1, 2, 3, 4],
    [1, 4, 2, 3]
]
with open('myfile.txt', 'w', encoding='utf-8') as file:
    for i in li:
        file.write(str(i) + '\n')

with open('myfile.txt') as file:
    for i in file:
