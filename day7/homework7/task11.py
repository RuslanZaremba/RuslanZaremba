# def decorator(func):
#     def wrapper(*args):
#         args = args[::-1]
#         func(*args)
#
#     return wrapper
#
#
# @decorator
# def nums(*args):
#     print(args)
#
#
# nums(1,2,3,4)

def decorator(func):
    def result(details, **kwargs):
        data = {}
        for i, j in kwargs.items():
            data[i] = j * details
        func(details, **data)

    return result


def obnull(func):
    def result(details, **kwargs):
        data = {}
        for i, j in kwargs.items():
            data[i] = 0 if j % 3 == 0 else j
        func(details, **data)

    return result


@obnull
@decorator
def nums(details, **kwargs):
    print(details)
    print(kwargs)


nums(details=3,
     a=1, b=2, c=3, d=4)
