# ДЛЯ ОТКРЫТИЯ ФАЙЛА
# my_file = open('test.txt', 'r', encoding='UTF-8')
# print(my_file)
# my_file.close()
#
# Вывод содержимого файла
# my_file = open('test.txt', encoding='UTF-8')
# print(my_file.read())
# my_file.close()
#
# Построчное чтение
# my_file = open('test.txt', encoding='UTF-8')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     print(line)
# my_file.close()
#
# Чтение всех строк файла
# my_file = open('test.txt', encoding='UTF-8')
# print(my_file.readlines())
# my_file.close()
#
# Открытие с помощью with тоже что и выше
# with open('test.txt', encoding='UTF-8') as my_file:
#     for line in my_file.readlines():
#         print(line)
#
# Построчная запись в файл
# with open('test.txt', 'w') as my_file:
#     my_file.write('qwerty')
#
# Запись в файл списка строк
# with open('test.txt', 'w') as my_file:
#     my_file.writelines(['hello\n', 'husein'])
#
# Дописывание в конец файла
# with open('test.txt', 'a') as my_file:
#     my_file.writelines(['privet\n', 'mir'])
#
#