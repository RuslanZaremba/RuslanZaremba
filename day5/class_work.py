import random

# def matrix(n):
#     data = []
#     for i in range(0, n):
#         stroka = []
#         for j in range(0, n):
#             stroka.append(random.randrange(1, 9))
#         data.append(stroka)
#     return data
#
# n = int(input())
# print(matrix(n))

# def matrix(n):
#     data = []
#     total = 0
#     tree = []
#     for i in range(0, n):
#         stroka = []
#         for j in range(0, n):
#             number = random.randrange(1, 100)
#             stroka.append(number)
#             if number % 3 == 0:
#                 tree.append(number)
#                 total += number
#         data.append(stroka)
#
#     return data, total, tree
#
#
# n = int(input())
# print(matrix(n))

# def matrix(n, m):
#     data = []
#     counter = 0
#     for i in range(0, n):
#         stroka = []
#         for j in range(0, m):
#             number = random.randrange(1, 9)
#             stroka.append(number)
#             if number == 7:
#                 counter += 1
#         data.append(stroka)
#     return data, counter
#
#
# n = int(input())
# m = int(input())
# print(matrix(n, m))

# for i, e in enumerate(['a', 'b', 'c', 'd']):
#     print(f"{i} - {e}")

# def matrix(n, m):
#     data = []
#     average = 0
#     for i in range(0, n):
#         stroka = []
#         for j in range(0, m):
#             number = random.randrange(1, 100)
#             average += number
#             stroka.append(number)
#         data.append(stroka)
#     average = average / (n * m)
#
#
#     counter = 0
#     for i in range(0, n):
#         for j in range(0, m):
#             if data[i][j] > average and (i + j) % 2:
#                 counter += 1
#     return data
#
#
# matrix(4, 5)


# n = int(input('От:'))
# m = int(input('До:'))
# counter = int(input('Количество попыток: '))
# number = random.randrange(1, 100)
# used = 0
#
# for i in range(counter):
#     user_number = int(input())
#
#     if user_number < n and user_number > m:
#         print(f"Number is not in range {n}-{m}")
#     if user_number == number:
#         correct = True
#         print('You are the winner.')
#         break
#
#     if correct is False:
#         print('You are the looser.')

# string = 'hello hello minsk moscow'
# words = {}
# longs_word = ""
# counter_word = string.split()[0]
# for i in string.split():
#     if len(longs_word) < len(i):
#         longs_word = i
#     if i in words:
#         words[i] += 1
#     else:
#         words[i] = 1
#     if counter_word not in words:
#         counter_word = i
#     if words[counter_word] < words[i]:
#         counter_word = i
# print(longs_word)
# print(words)
# print(counter_word)
l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 3, 1, 9, 10, 12]


def checker(a, b):
    for i in a:
        if i not in b:
            print(i)


checker(l1, l2)
