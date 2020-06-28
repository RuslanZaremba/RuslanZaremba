class Dog:
    def __init__(self):
        print('Собака создана')

    def jump(self):
        print('Jump')
    def run(self):
        print('Run')

dog_1 = Dog()
dog_2 = Dog()

dog_1.jump()
dog_2.run()