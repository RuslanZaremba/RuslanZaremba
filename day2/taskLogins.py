print('Длина должна быть от 1 до 10 символов')
login_in = input('Введите ваш логин для проверки: ')

if 1 <= len(login_in) <= 10 and login_in[0:2] == 'io' and login_in[2:].isdigit():
    print('Correct')
else:
    print('Incorrect')
