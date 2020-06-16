# with open('task4.txt') as file:
#     with open('task4_new.txt', 'w') as new_file:
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
