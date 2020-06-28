class Pet:
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

    def birthday(self, year=1):
        self.age += year


class Dog(Pet):

    def bark(self):
        print('Gav-Gav')


class Cat(Pet):

    def meow(self):
        print('Meow-Meow')


class Parrot(Pet):

    def fly(self):
        print('Parrot is flying')


dog = Dog('Jack-Russel', 3, 'Olga')
print(f"{dog.name}, {dog.age}, {dog.master}")
dog.run()
dog.jump()
dog.sleep()
dog.bark()
dog.birthday()
print(f"{dog.name}, {dog.age}, {dog.master}\n")
cat = Cat('Siam', 4, 'Ivan')
print(f"{cat.name}, {cat.age}, {cat.master}")
cat.run()
cat.jump()
cat.sleep()
cat.meow()
cat.birthday()
print(f"{cat.name}, {cat.age}, {cat.master}\n")
parrot = Parrot('Gosha', 1, 'Ruslan')
print(f"{parrot.name}, {parrot.age}, {parrot.master}")
parrot.run()
parrot.jump()
parrot.sleep()
parrot.fly()
parrot.birthday()
print(f"{parrot.name}, {parrot.age}, {parrot.master}")
