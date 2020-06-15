# 10. Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
def decorator(func):
    def wrapper(*args):
        fu = func(*args)
        result = list(filter(lambda x: x % 2, fu))
        return print(result)

    return wrapper


@decorator
def nums(num):
    return num


print(nums([1, 2, 3, 4, 5, 6, 7]))
