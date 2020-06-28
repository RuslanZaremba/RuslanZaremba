class Pet:
    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height

    def run(self):
        print('Run')

    def jump(self, x):
        print(f"Прыгнул на  {x} метр.")

    def sleep(self):
        print('Sleep')

    def birthday(self, year=1):
        self.age += year

    def voice(self):
        pass

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

    def voice(self):
        print('Gav-Gav')

    def jump(self, jump):
        if jump > 0.5:
            print('Собака не может прыгать так высоко!')
        else:
            print(f"Собака прыгнула на  {jump} метр.")


class Cat(Pet):

    def voice(self):
        print('Meow-Meow')

    def jump(self, jump):
        if jump > 2:
            print('Кошка не может прыгать так высоко!')
        else:
            print(f"Кошка прыгнула на  {jump} метр.")


class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def change_weight(self, increase_weight=0.05):
        self.weight += increase_weight

    def change_height(self, increase_height=0.2):
        self.height += increase_height

    def jump(self, jump):
        if jump > 0.05:
            print('Попугай не может прыгать так высоко!')
        else:
            print(f"Попугай прыгнул на  {jump} метр.")

    def fly(self):
        if self.weight > 0.2:
            print('This parrot cannot fly')
        else:
            print('Parrot is flying')

    def voice(self):
        print('Kra-Kra')


parrot = Parrot('Gosha', 1, 'Ruslan', 0.1, 2, 'species')
cat = Cat('murzic', 2, 'Olga', 4, 2)
dog = Dog('Djack', 4, 'Tatsiana', 8, 7)
pet_list = [parrot, cat, dog]


def voice_func(*args):
    for i in args:
        i.voice()


def vo(pet_list):
    for i in pet_list:
        i.voice()


vo(pet_list)
voice_func(parrot, cat, dog)
