def decorator(func):
    def wrapper(a, b):
        split = func(b, a)
        result = split
        return print(result)

    return wrapper


@decorator
def nums(a, b):
    return a - b


print(nums(1, 2))
