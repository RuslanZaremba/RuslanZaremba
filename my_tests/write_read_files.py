# ЗАПИСЬ В ФАЙЛ
# vvod = input('Введите то что хотите добавить в файл: ')
# with open('file_for_writing.txt', 'w', encoding='utf-8') as file:
#     # АРГУМЕНТ СТРОКА
#     file.write(vvod)
#     file.write('string\n')
#     # Аргумент может быть строка и список
#     file.writelines(['srting1 ', 'string2 ', 'string3 '])

# ЧТЕНИЕ ИЗ ФАЙЛА
# with open('file_for_writing.txt', 'r', encoding='utf-8') as file:
#     file_read = file.read()
# print(file_read)
#
# with open('file_for_writing.txt', 'r', encoding='utf-8') as file:
#     file_readline = file.readline()
# print(file_readline)
#
# with open('file_for_writing.txt', 'r', encoding='utf-8') as file:
#     file_readlines = file.readlines()
# # print(file_readlines)

# ЧТЕНИЕ ИЗ ФАЙЛА Построчное
# with open('file_for_writing.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line, end='')
with open('file_for_writing.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line)
