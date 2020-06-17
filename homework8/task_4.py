# with open('task4.txt') as file:
#     with open('task4_new.txt', 'w') as new_file:
<<<<<<< HEAD
#         new_file.write(file.read())
#         print(type(file.read()))
# a = '10101'
# print(a)
# b = list(map(lambda x: 1 if int(x) == 0 else 0, a))
# print(''.join(b))
with open('text_files/task4.txt') as file:
    with open('text_files/task4_new.txt', 'w') as new_file:
        for line in file:
            for i in line:
                if i.isdigit():
                    i = map(lambda x: 1 if int(x) == 0 else 0)
            # new_list = list(map(lambda x: 1 if int(x) == 0 else 0, line))
            # new_row = ''.join(map(lambda x: str(x)
            # new_file.write(new_list)
=======
#         for i in file.read():
#             if i.isdigit():
#                 b = list(map(lambda x: 1 if int(x) == 0 else 0, i))
#                 new_file.write(''.join(map(str, b)))
#             else:
#                 continue

with open('task4.txt') as file:
    with open('task4_new.txt', 'w') as new_file:
        for i in range(len(file.read())-1):
            print(i)

