import csv

# ЗАПИСЬ CSV Таблиц
fields = ['firstname', 'lastname', 'group']
rows = [
    ['Alex', 'Varkalov', 'Z-21'],
    ['Max', 'Ivanov', 'Z-21']
]
filename = "students_info.csv"
with open(filename, 'w') as csfile:
    csvwriter = csv.writer(csfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)


# Чтение CSV Таблиц
rows = []
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        print('Total no. of rows:%d' % (csvreader.line_num))
    for col in fields:
        print("%10s" % col, end='')
    print()
    for row in rows[:5]:
        for col in row:
            print("%10s" % col, sep='', end='')
        print()
