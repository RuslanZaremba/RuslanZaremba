class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def sleep(self):
        print('Sleep')

    def birthday(self, year=1):
        self.age += year

    # def change_weight(self, increase_weight=0.2):
    #     self.weight += increase_weight
    #
    # def change_height(self, increase_height=0.2):
    #     self.height += increase_height

    @property
    def change_weight(self):
        return self.weight

    @change_weight.setter
    def change_weight(self, increase_weight=0.2):
        self.weight += increase_weight

    @property
    def change_height(self):
        return self.height

    @change_height.setter
    def change_height(self, increase_height=0.2):
        self.height += increase_height


class Dog(Pet):

    def bark(self):
        print('Gav-Gav')


class Cat(Pet):

    def meow(self):
        print('Meow-Meow')


class Parrot(Pet):

    def fly(self):
        if self.weight > 0.2:
            print('This parrot cannot fly')
        else:
            print('Parrot is flying')


parrot = Parrot('Gosha', 1, 'Ruslan', 0.1, 2)

parrot.fly()
parrot.change_weight = 0.2
parrot.fly()
print(f"{parrot.name}, {parrot.age}, {parrot.master}, {parrot.weight}")
