money = float(input('Введите количество рублей: '))

if len(str(money).split('.')[1]) > 2:
    print('Количество копеек не может превышать 99')
else:
    num_rub = int(str(money).split('.')[0][-2::])
    num_kop = float('0' + '.' + str(money).split('.')[1])
    name_rub = ''
    name_kop = ''
    if num_rub == 1 or num_rub % 10 == 1 and num_rub != 11:
        name_rub = 'рубль'
    elif int(str(money).split('.')[0][-1]) in [2, 3, 4] and int(str(money).split('.')[0][-2::]) not in [12, 13, 14]:
        name_rub = 'рубля'
    else:
        name_rub = 'рублей'
    if num_kop == 0.01 or int(num_kop * 100 % 10) == 1 and num_kop != 0.11:
        name_kop = 'копейка'
    elif num_kop in [0.2, 0.3, 0.4]:
        name_kop = 'копейки'
    else:
        name_kop = 'копеек'
    print(f"{num_rub} {name_rub} {str(money).split('.')[1]} {name_kop}")
