def funct_2or8(a, b):
    num_converted = []
    if b == 8:
        i = a
        while i != 0:
            num_converted.insert(0, i % 8)
            i = i // 8
    elif b == 2:
        i = a
        while i != 0:
            num_converted.insert(0, i % 2)
            i = i // 2
    return print(''.join(map(str, num_converted)))


a = int(input('введите число для конвертации: '))
b = int(input('Введите систему счисления 2 для двоичной, 8 для восьмиричной: '))
funct_2or8(a, b)
