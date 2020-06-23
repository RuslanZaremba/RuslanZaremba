class Dog:
    def __init__(self, name, age, height, weight):
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age

    @property
    def get_height(self):
        return self._height

    @property
    def get_weight(self):
        return self._weight

    @get_name.setter
    def set_name(self, new_name):
        self._name = new_name

    @get_age.setter
    def set_age(self, new_age):
        self._age = new_age

    @get_height.setter
    def set_height(self, new_height):
        self._height = new_height

    @get_weight.setter
    def set_weight(self, new_weight):
        self._weight = new_weight
