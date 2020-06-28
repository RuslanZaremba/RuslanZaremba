class Dog:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self._master = master

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print('Gav-Gav')

    def change_name(self, new_name):
        self.name = new_name

    def get_master(self):
        return self._master


dog_1 = Dog('NIka', 6, 30, 5)
print(f"Name: {dog_1.name}")
print(f"Name: {dog_1.name}, age: {dog_1.age} , height: {dog_1.height}, weight: {dog_1.weight}")
dog_1.change_name('Tobby')
print(f"Name: {dog_1.name}")
print(f"Name: {dog_1.name}, age: {dog_1.age} , height: {dog_1.height}, weight: {dog_1.weight}")