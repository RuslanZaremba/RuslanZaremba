"""1. Создать csv файл с данными следующей структуры:
Имя, Фамилия, Возраст. Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
 Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
"""
import csv

def saver(file, *args):
    with open(file, 'a+', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(*args)


# def find(row, min, max=99):
#     group = []
#     if min <= int(row[2]) <= max:
#         group.append(row)
#         return group


with open('text_files/text_1_1.csv', newline='') as file:
    reader = csv.reader(file)
    group1_12 = []
    group13_18 = []
    group19_25 = []
    group26_40 = []
    group41_99 = []
    for index, row in enumerate(list(reader)):
        if index != 0:
            if 1 <= int(row[2]) <= 12:
                group1_12.append(row)
            elif 13 <= int(row[2]) <= 18:
                group13_18.append(row)
            elif 19 <= int(row[2]) <= 25:
                group19_25.append(row)
            elif 26 <= int(row[2]) <= 40:
                group26_40.append(row)
            else:
                group41_99.append(row)
print(f"В группе от 1 до 12: {len(group1_12)} позиции.")
print(f"В группе от 13 до 18: {len(group13_18)} позиции.")
print(f"В группе от 19 до 25: {len(group19_25)} позиции.")
print(f"В группе от 26 до 40: {len(group26_40)} позиции.")
print(f"В группе от 40+: {len(group41_99)} позиции.")
