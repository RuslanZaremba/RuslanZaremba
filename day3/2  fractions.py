a = int(input('числитель первой дроби: '))
b = int(input('знаменатель первой дроби: '))
c = int(input('числитель второй дроби: '))
d = int(input('числитель второй дроби: '))

if a / b > c / d:
    print('1')
elif a / b < c / d:
    print('-1')
else:
    print('0')
