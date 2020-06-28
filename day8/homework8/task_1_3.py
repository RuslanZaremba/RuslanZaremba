from datetime import datetime
import csv

data = ['12.02.2020', '01.03.2020', '31.01.2020']
# with open('text_files/task_1_3.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(data)

with open('text_files/task_1_3.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        true_time = list(map(lambda x: x.replace('.', ' '), row))
        time_true_format = list(map(lambda x: datetime.strptime(x, "%d %m %Y"), true_time))
        print(f"Минимальная дата в списке: {min(time_true_format)}")
