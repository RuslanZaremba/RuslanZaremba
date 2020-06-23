class Dog:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print('Gav-Gav')


dog_1 = Dog('NIka', 6, 30, 5)
dog_1.jump()
dog_1.run()
dog_1.bark()
print(f"Name: {dog_1.name}, age: {dog_1.age} , height: {dog_1.height}, weight: {dog_1.weight}")
