i = int(input('Введите число для вычисления факториала: '))
a = i
factorial = 1
while i > 1:
    factorial *= i
    i -= 1
print(a, '!=', factorial)
