import math

a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третюю сторону треугольника: '))

half_perimeter = (a + b + c) / 2
s = math.sqrt(half_perimeter)
print('Площадь треугольника со сторонами: ', a, b, c, 'равна: ', s)
