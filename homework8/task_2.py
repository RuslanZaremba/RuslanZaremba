with open('task2.txt', 'w', encoding='UTF-8') as task2:
    while True:
        data = input('Введите строку для записи: ')
        task2.writelines(data + '\n')
        if data == '':
            break