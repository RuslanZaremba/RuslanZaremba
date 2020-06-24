import json
class Dog:
    file = None

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.data = []

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print('Gav-Gav')

    def read(self):
        with open("text_files/task_4.txt", 'r', encoding='utf-8') as data:
            data = data.readlines()
            for i in data:
                value = i.replace("\n", '').split(' ')
                self.data.append({
                    'name': value[0],
                    'age': value[1],
                    'height': value[2],
                        'weight': value[3]
                })

    def give_by_name(self, name):
        for i in self.data:
            if name == i.get('name'):
                print(i)

    def add(self):
        self.data.append({
            'name': self.name,
            'age': self.age,
            'height': self.height,
            'weight': self.weight
        })
    def save(self):
        with open('text_files/task_4.json', 'a') as json_file:
            json_file.writelines(json.dumps(self.data))

    def open(self):
        with open('text_files/task_4.json', 'r', encoding="UTF-8") as json_file:
            data = json.loads(json_file.read())
            for i in data:
                self.data.append(i)

d = Dog('asd.', 5, 7, 2)
# Dog.read('text_files/task_4.txt')
d.add()
# d.save()
d.open()
dog_1 = Dog('NIka', 6, 30, 5)
# dog_1.read()
# dog_1.give_by_name('Собака1')
# dog_1.jump()
# dog_1.run()
# dog_1.bark()
# print(f"Name: {dog_1.name}, age: {dog_1.age} , height: {dog_1.height}, weight: {dog_1.weight}")
