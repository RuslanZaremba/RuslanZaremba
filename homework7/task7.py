def benchmark(func):
    from datetime import datetime

    def wrapper():
        start = datetime.now()
        func()
        finish = datetime.now()
        print('2 Время выполнения функции: {}'.format(finish - start))

    return wrapper


def bench(func):
    def wrapper():
        print('Второй декоратор')
        func()
    return wrapper


@bench
@benchmark
def hello():
    import random
    data = [random.randrange(0, 2 ** 100) for i in range(0, 2 ** 20)]
    total = sorted(data)
    return total


hello()
