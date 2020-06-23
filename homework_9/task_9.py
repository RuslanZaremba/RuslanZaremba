class Dog():
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def sleep(self):
        print('Sleep')

    def bark(self):
        print('Gav-Gav')

# но аргумент полюбому передавать нужно типа dog.birthday = 1
    # @property
    # def birthday(self):
    #     return self.age
    #
    # @birthday.setter
    # def birthday(self, year=1):
    #     self.age += year

    def birthday(self, year=1):
        self.age += year



class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def sleep(self):
        print('Sleep')

    def meow(self):
        print('Meow-Meow')

# но аргумент полюбому передавать нужно типа dog.birthday = 1
    # @property
    # def birthday(self):
    #     return self.age
    #
    # @birthday.setter
    # def birthday(self, age=None):
    #     self.age += 1

    def birthday(self, year=1):
        self.age += year
class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print('Run')

    def jump(self):
        print('Jump')

    def sleep(self):
        print('Sleep')

    def fly(self):
        print('Parrot is flying')

# но аргумент полюбому передавать нужно типа dog.birthday = 1
    # @property
    # def birthday(self):
    #     return self.age
    #
    # @birthday.setter
    # def birthday(self, age=None):
    #     self.age += 1

    def birthday(self, year=1):
        self.age += year

dog = Dog('Fu', 12, 'Ruslan')
print(f'{dog.name} {dog.age} {dog.master}')
dog.birthday()
print(f'{dog.name} {dog.age} {dog.master}')
