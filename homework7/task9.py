# Создать lambda функцию, которая принимает на вход неопределенное количество
# именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}
di = {'a': 2,'b':3}
# func = [(lambda i, y: {i * 2: y})(key, value) for key, value in di.items()]
for key, value in di.items():
    print((lambda i, y: {i * 2: y})(key, value))
