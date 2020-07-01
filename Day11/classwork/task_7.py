from time import sleep
import random


def simple_gen():
    while True:
        sleep(1)
        yield random.randint(1, 100)


gen = simple_gen()
while True:
    sleep(1)
    print(next(simple_gen()))
