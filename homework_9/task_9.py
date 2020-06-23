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

    @property
    def birthday(self):
        return self.age

    @birthday.setter
    def birthday(self, age):
        self.age += 1

#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#

dog = Dog('Fu', 12, 'Ruslan')
print(f'{dog.name} {dog.age} {dog.master}')
dog.birthday
print(f'{dog.name} {dog.age} {dog.master}')
