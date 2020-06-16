import json

# Добавление в файл
with open('test.txt', 'w') as my_file:
    data = json.dumps({'a': 5})
    my_file.write(data)
# Распаковка из файла
with open('test.txt', 'r') as my_file:
    data = json.loads(my_file.read())
    print(data)
