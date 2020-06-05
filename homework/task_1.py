# def average(a, b):
#     """
#     Задача №1
#     Функция возвращает среднее арифметическое 2х аргументов.
#     :param a: первое число
#     :type: float
#     :param b: второе число
#     :type: float
#     :return: среднее арифметическое a и b
#     :type: float
#     """
#     return print((a + b) / 2)
#
#
# average(2.5, 4)

# def fx(*nums):
#     """
#     Задача №2
#     Среди вычисленных значений аргументов находит наибольшее.
#     :param nums:
#     :type:  float, int
#     :return:Среди вычисленных значений аргументов находит наибольшее
#     :type:  float, int
#     """
#     li = []
#     for x in nums:
#         if -2 <= x < 2:
#             a = x ** 2
#         elif x >= 2:
#             a = x ** 2 + 4 * x + 5
#         else:
#             a = 4
#         li.append(a)
#     print(li)
#     return max(li)
#
#
# print(fx(2.3, 5.1, 6.9))

