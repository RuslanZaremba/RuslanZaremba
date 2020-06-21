"""2. Создать csv файл с данными о ежедневной погоде. Структура:  Дата, Место, Градусы, Скорость ветра.
Найти среднюю погоду(скорость ветра и градусы) для Минск за последние 7 дней."""
import csv


def mean(dannie, key, days):
    """
    Считает среднее значение по заданному ключу списка словарей.
    :param dannie: Ваш список словарей с данными
    :type: list
    :param key: Название колонки у которой нужно узнать средний результат
    :type: str
    :param days: Количество дней по которые нужно узнать средние данные
    :type: int
    :return: Среднее значение
    :type: int
    """
    nums = []
    for index, row in enumerate(dannie, 1):
        if index == days:
            break
        else:
            nums.append(int(row[key]))
    return sum(nums) / len(nums)


data = [
    {'Date': '01.06.2020', 'Place': 'Minsk', 'Degree': 23, 'Speed of wind': 2},
    {'Date': '02.06.2020', 'Place': 'Minsk', 'Degree': 32, 'Speed of wind': 4},
    {'Date': '03.06.2020', 'Place': 'Minsk', 'Degree': 12, 'Speed of wind': 1},
    {'Date': '04.06.2020', 'Place': 'Minsk', 'Degree': 15, 'Speed of wind': 5},
    {'Date': '05.06.2020', 'Place': 'Minsk', 'Degree': 18, 'Speed of wind': 6},
    {'Date': '06.06.2020', 'Place': 'Minsk', 'Degree': 33, 'Speed of wind': 9},
    {'Date': '07.06.2020', 'Place': 'Minsk', 'Degree': 30, 'Speed of wind': 4}
]

with open('text_files/weather.csv', 'w', newline="") as weather:
    writer = csv.DictWriter(weather, fieldnames=list(data[0].keys()))
    writer.writeheader()
    writer.writerows(data)

with open('text_files/weather.csv', 'r', newline="") as weather:
    reader = csv.DictReader(weather)
    reader = list(reader)
    print(f"Средние значения за 7 дней:\n"
          f"Градусы: {mean(reader, 'Degree', 7)} \n"
          f"Скорость ветра м/с: {mean(reader, 'Speed of wind', 7)}")
