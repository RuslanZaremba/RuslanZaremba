class Car:
    def __init__(self):
        self.odometr = 0


car = Car()
car.odometr = 9
print(car.odometr)


class Electric(Car):
    def __init__(self):
        super().__init__()


elcar = Electric()
elcar.odometr += 100
print(elcar.odometr)
