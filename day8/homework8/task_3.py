with open('text_files/task2.txt', 'a', encoding='UTF-8') as task2:
    while True:
        data = input('Введите строку для добавления в файл: ')
        task2.write('\n' + data)
        if data == '':
            break
