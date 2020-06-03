"""​Вычислить квадратное уравнение ax2 + bx + c = 0 (*)​
D = b2 – 4ac; ​
x1,2 = (-b +/- sqrt (D)) / 2a​
Предусмотреть 3 варианта:​
Два действительных корня​
Один действительный корень​
Нет действительных корней​
​"""
import math

a = int(input())
b = int(input())
c = int(input())
try:
    d = b ** 2 - 4 * a * c
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)

    if x1 != x2:
        print(f"x1: {x1} x2: {x2}")
    elif x1 == x2:
        print(f"x1, x2 = {x1}")
except:
    print('No')
