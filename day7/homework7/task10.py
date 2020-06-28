# 10. Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
# def decorator(func):
#     def wrapper(*args):
#         fu = func(*args)
#         result = list(filter(lambda x: x % 2, fu))
#         return print(result)
#
#     return wrapper
#
#
# @decorator
# def nums(num):
#     return num
#
#
# print(nums([1, 2, 3, 4, 5, 6, 7]))


# def decorate(func):
#     def results(datas):
#         result = []
#         for i in datas:
#             if not i % 2 == 0:
#                 result.append(i)
#         func(result)
#     return results
#
# @decorate
# def result(datas):
#     print(datas)

# result([1, 2, 3, 4])


def decorate(func):
    def results(datas):
        result = {}
        for i, j in enumerate(datas, 1):
            result[j] = i
        func(result)

    return results


@decorate
def result(datas):
    print(datas)


result(['a', 'b', 'c', 'd'])
