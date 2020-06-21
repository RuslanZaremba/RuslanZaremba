"""1. Создать csv файл с данными следующей структуры:
Имя, Фамилия, Возраст. Создать отчетный файл с информацией по количеству людей входящих в ту или иную возрастную группу.
 Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
"""
import csv


def saver(file, *args):
    with open(file, 'a+', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(*args)

def find(row, min, max):
    group = []
    if min <= int(row[2]) <= max:
        group.append(row)
        return group

with open('text_files/text_1_1.csv', newline='') as file:
    reader = csv.reader(file)
    for index, row in enumerate(list(reader)):
        if index != 0:
            group1_12 = find(row, 1, 12)
print(group1_12)

# with open('text_files/text_1_1_result.csv', 'w', newline='') as file_new:
#     writer = csv.writer(file_new)
