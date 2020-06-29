# class Car:
#     last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.last_model = model
#
#     @property
#     def get_lastmodel(self):
#         return Car.last_model
#
#     @get_lastmodel.setter
#     def get_lastmodel(self, new_last_model):
#         Car.last_model = new_last_model
#
# obj = Car(1)
# obj.get_lastmodel = 4

# print(obj.get_lastmodel)


# class Car:
#     last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.last_model = model
#
#     @classmethod
#     def get_last_model(cls, new_last_model=None):
#         if new_last_model is not None:
#             cls.last_model = new_last_model
#         return cls.last_model
#
#     @staticmethod
#     def is_model_ok(model):
#         return len(model) > 3
#
#
# car = Car('Audi')
# print(Car.get_last_model(3))
# print(Car.is_model_ok('ruslan'))

# a = int(input('a: '))
# b = int(input('b: '))
# try :
#     res = a/b
# except ZeroDivisionError as err:
#     print(f"b is zero - {err}!!!")
# except Exception as err:
#     print(f"SOMETHING WRONG - {err}!!!")
# else:
#     print('Ошибок небыло.')
# finally:
#     print('Сработает всегда.')

# a = int(input('a: '))
# b = int(input('b: '))
#
# if b == 0:
#     raise ZeroDivisionError('b is zero')

# class MyException(Exception):
#     def __init__(self, message='AAA!!!'):
#         super().__init__(message)
#
# raise MyException