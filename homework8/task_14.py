import csv

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open('text_files/task_14.csv', 'w', newline='') as file_csv:
    colomns = ['name', 'age']
    writer = csv.DictWriter(file_csv, fieldnames=colomns)
    writer.writeheader()
    writer.writerows(users)

with open('text_files/task_14.csv', newline='') as file_csv:
    reader = csv.DictReader(file_csv)
    for row in reader:
        print(f"{row['name']} - {row['age']}")
