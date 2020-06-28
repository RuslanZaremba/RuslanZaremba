# Написать функции по работе с csv файлами в файле csv_utils.py.
# Чтение. Запись. Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).
from homework8.task8.csv_utils import saver, readers, remover

# saver('data.csv', ['Ruslan', "Zaremba", 7])
# saver('data.csv', [1, "lp", 3], 2)
# remover('data.csv', 2)
remover('data.csv', 0)
