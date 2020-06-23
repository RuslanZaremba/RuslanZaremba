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

    @property
    def birthday(self):
        return self.age

    @birthday.setter
    def birthday(self, age=None):
        self.age += 1
