"""Ввести число, проверить на то, что было введено именно число. Возвести его в куб."""
a = input('Введите число: ')
if a in '1234567890':
    a = int(a) ** 3
    print(a)