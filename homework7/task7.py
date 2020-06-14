def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print('Время выполнения функции: {}'.format(finish-start))
    return wrapper
@benchmark
def hello():
    print('hello')
hello()