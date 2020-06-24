class Car:
    def __init__(self, made, model, year):
        self.__made = made
        self.__model = model
        self.__year = year
        self.__speed = 0
        print(f"Автомобиль {self.__made} создан.")

    def speed_Indication(self):
        print(f"Текущая скорость: {self.__speed} км/ч.")

    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def reverce(self):
        if self.__speed > 0:
            self.__speed = -(self.__speed)


car = Car('audi', 'tt', 2020)

car.speed_down()
car.speed_down()
car.reverce()
car.speed_Indication()
