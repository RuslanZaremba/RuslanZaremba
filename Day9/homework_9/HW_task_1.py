from datetime import datetime
class Bank:
    def __init__(self, name, sity, index):
        self.__name = name
        self.__sity = sity
        self.__index = index
        print(f"Банк {self.__name} создан.")

    def greeting(self):
        print(f"Вас приветствует {self.__name} банк.")

    def append_country_for_sity(self, country):
        self.__sity += f" ,{country}"

    @property
    def get_name(self):
        return self.__name

    @property
    def get_sity(self):
        return self.__sity

    @property
    def get_index(self):
        return self.__index

    @get_name.setter
    def set_name(self, new_name):
        self.__name = new_name

    @get_sity.setter
    def set_sity(self, new_sity):
        self.__sity = new_sity

    @get_index.setter
    def set_index(self, new_index):
        self.__index = new_index


# bank = Bank('MTB', 'Minsk', 220100)
# bank.append_country_for_sity('RB')
# print(bank._Bank__sity)


class Person:
    def __init__(self, name, lastname, id):
        self.__name = name
        self.__lastname = lastname
        self.__id = id
        self.communication = {}
        print(f"Человек {self.__name} {self.__lastname} создан.")

    def communication_inpnut(self, status, name):
        """
        Добавляем связи, окружение человека по отношению()
        :param status: Друзья, Родные и т.д. социальные контакты.
        :type: str
        :param name: Имя
        :type: str
        :return: Словарь окружения со списками имен.
        :type: dict
        """
        status = status.lower()
        if status not in self.communication.keys():
            self.communication.setdefault(status, [name])
        else:
            self.communication[status].append(name)

    def find_communication(self, status):
        """
        Ищет связи по статусу
        :param status: например wife, friends
        :type: str
        :return: список имен
        :type: list
        """
        status = status.lower()
        print(self.communication.get(status))

    @property
    def get_name(self):
        return self.__name

    @property
    def get_lastname(self):
        return self.__lastname

    @property
    def get_id(self):
        return self.__id

    @get_name.setter
    def set_name(self, new_name):
        self.__name = new_name

    @get_lastname.setter
    def set_lastname(self, new_lastname):
        self.__lastname = new_lastname

    @get_id.setter
    def set_id(self, new_id):
        self.__id = new_id


# man = Person('Ruslan', 'Zaremba', 3215321)
# man.communication_inpnut('wife', 'Tanya Zaremba')
# man.communication_inpnut('FRIends', 'Kris')
# man.communication_inpnut('frienDs', 'Bob Tod')
# man.find_communication('Friends')


class Private_Chat:
    def __init__(self, name, theme, counter):
        self.__name = name
        self.__theme = theme
        self.__counter = counter
        print(f"Чат {self.__name} создан.")

    def counter_increase(self, value):
        self.__counter += value

    def congrats(self):
        if self.__counter == 1:
            print(f"Поздравляем, вы первфй человек в чате.")
        elif self.__counter >= 1000000:
            print(f"Поздравляем, Нас уже миллион.")
        elif self.__counter >= 1000:
            print(f"Нас уже Одна тысяча.")

    @property
    def get_name(self):
        return self.__name

    @property
    def get_theme(self):
        return self.__theme

    @property
    def get_counter(self):
        return self.__counter

    @get_name.setter
    def set_name(self, new_name):
        self.__name = new_name

    @get_theme.setter
    def set_theme(self, new_theme):
        self.__theme = new_theme

    @get_counter.setter
    def set_counter(self, new_counter):
        self.__counter = new_counter


# chat = Private_Chat('chat', 'animals', 0)
# chat.set_counter = 1
# chat.counter_increase(1000)
# print(f"В {chat.get_name} по теме {chat.get_theme} уже {chat.get_counter} чел.")
# chat.congrats()


class Car:
    def __init__(self, made, model, year):
        self.__made = made
        self.__model = model
        self.__year = year
        print(f"Автомобиль {self.__made} создан.")

    def start(self):
        print(f"Зажигание вкл.")

    def finish(self):
        print(f"Зажигание выкл.")

    @property
    def get_made(self):
        return self.__made

    @property
    def get_model(self):
        return self.__model

    @property
    def get_year(self):
        return self.__year

    @get_made.setter
    def set_made(self, new_made):
        self.__made = new_made

    @get_model.setter
    def set_model(self, new_model):
        self.__model = new_model

    @get_year.setter
    def set_year(self, new_year):
        self.__year = new_year


class Weather:

    def __init__(self, degrees, wind, humidity):
        self.__degrees = degrees
        self.__wind = wind
        self.__humidity = humidity
        self.history_of_dates = []
        print(f'Погода на {datetime.now().strftime("%d %m %Y")}.')

    def normal_weather(self):
        if 20 < self.__degrees < 25 and 0 < self.__wind < 5 and 40 < self.__humidity < 75:
            print(f"Сегодня нормальная погода.")
        else:
            print(f"Погода не оптимальная.")

    def database(self):
        self.history_of_dates.append([datetime.now().strftime("%d %m %Y")])

    @property
    def get_degrees(self):
        return self.__degrees

    @property
    def get_wind(self):
        return self.__wind

    @property
    def get_humidity(self):
        return self.__humidity

    @get_degrees.setter
    def set_degrees(self, new_degrees):
        self.__degrees = new_degrees

    @get_wind.setter
    def set_wind(self, new_wind):
        self.__wind = new_wind

    @get_humidity.setter
    def set_year(self, new_humidity):
        self.__humidity = new_humidity


weather = Weather(24, 3, 50)
weather.database()
print(weather.history_of_dates)
