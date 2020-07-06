import function

work = True
while work:
    znak = input('Введите знак(для остановки введите stop.): ')
    if znak == 'stop':
        work = False
        break
    a = float(input('Введите число: '))
    b = float(input('Введите число: '))
    if znak == '+':
        print(function.add(a, b))
    elif znak == '-':
        print(function.min(a, b))
    elif znak == '*':
        print(function.mul(a, b))
    elif znak == '/':
        print(function.delen(a, b))
