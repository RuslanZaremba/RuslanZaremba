list_a = [1, 2, 3, 4]
list_b = []
print('ID a', id(list_a), 'ID b', id(list_b))

list_b = list_a

for i in list_a:
    print('ID переменных a: ', id(i))
for i in list_b:
    print('ID переменных b: ', id(i))
list_b.append(5)

print(list_a, list_b)
"""ВЫВОД ОДИНАКОВЫЙ ПОТОМУ ЧТО ПЕРЕМЕННЫЕ 
                        ССЫЛАЮТСЯ НА ОДИН СПИСОК"""
