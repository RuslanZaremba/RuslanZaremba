import csv

fields = ['firstname', 'lastname', 'group']
rows = [
    ['Alex', 'Varkalov', 'Z-21'],
    ['Max', 'Ivanov', 'Z-21']
]
filename = 'test.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)

with open(filename, 'a') as file:
    writer = csv.writer(file)
    writer.writerow(['Ruslan', 'Zaremba', 'z-31'])