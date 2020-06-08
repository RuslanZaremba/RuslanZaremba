# Считаем факториал
i = int(input('Введите число для вычисления факториала: '))
if i == 0:
    print(i, '!=', 1)
    quit()

a = i
factorial = 1
while i > 1:
    factorial *= i
    i -= 1
print(a, '!=', factorial)

