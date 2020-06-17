# with open('text_files/task6.txt', encoding='UTF-8') as first1:
#     with open('text_files/task6_2.txt', encoding='UTF-8') as second1:
#         first = first1.readlines()
#         second = second1.readlines()
#         for i in range(len(first)):
#             if first[i] != second[i]:
#                 print(i)

data1 = [1, 2, 3, 4, 5]
data2 = [5, 4, 3, 2, 1]
for i, j in enumerate(zip(data1, data2)):
    print(i, j)
