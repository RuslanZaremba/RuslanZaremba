# Считаем факториал
i = int(input('Введите число для вычисления факториала: '))
a = i
factorial = 1
if i == 0 or i == 1:
    factorial = 1
else:
    while i > 1:
        factorial *= i
        i -= 1
print(a, '!=', factorial)
