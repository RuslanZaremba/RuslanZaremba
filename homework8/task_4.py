# with open('task4.txt') as file:
#     with open('task4_new.txt', 'w') as new_file:
#         new_file.write(file.read())
#         print(type(file.read()))
a = '10101'
print(a)
b = list(map(lambda x: 1 if int(x) == 0 else 0, a))
print(str(map(str(b),b)))
