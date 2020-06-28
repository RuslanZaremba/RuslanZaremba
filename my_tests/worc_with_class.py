# КЛАСС МЕТОД
from abc import ABC, abstractclassmethod


# class Car:
#     __last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.__last_model = model
#
#     @classmethod
#     def get_last_model(cls):
#         return cls.__last_model
#
#
# car1 = Car('BMW')
# print(car1.model)
# print(Car.get_last_model())

# СТАТИК МЕТОД\

# class Car:
#     __last_model = None
#     def __init__(self, model):
#         self.model = model
#         Car.__last_model = model
#
#     @staticmethod
#     def is_model_ok(model):
#         return len(model) > 3
#
# print(Car.is_model_ok('abc'))

# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ

# class A:
#     def print_smth(self):
#         print('A')
#
#     def a_method(self):
#         print('a method')
#
#
# class B(A):
#     def print_smth(self):
#         print('B')
#
#     def b_method(self):
#         print('b method')
#
#
# class C(A):
#     def print_smth(self):
#         print('C')
#
#     def c_method(self):
#         print('c method')
#
#
# class D(B, C):
#
#     def d_method(self):
#         print('d method')
#
#
# d = D()
# d.b_method()
# d.c_method()
# d.d_method()

# Абстрактный класс

# class A(ABC):
#     @abstractclassmethod
#     def do_smth(self):
#         print('I am a parent.')
# class B(A):
#     def do_smth(self):
#         print('I am child.')
#
# a = A()
# b = B()

# ИНТЕРФЕЙСЫ
# class MyInterface(ABC):
#     @abstractclassmethod
#     def do_a(self, arg1):
#         raise NotImplemented
#
#     @abstractclassmethod
#     def do_b(self, arg1, arg2):
#         raise NotImplemented
#
#
# class MyClass(MyInterface):
#     def do_a(self, arg1):
#         print(arg1)
#
#     def do_b(self, arg1, arg2):
#         print(arg1, arg2)
#
# myclass = MyClass()
# myclass.do_a('a')
# myclass.do_b('a', 'b')

# Миксины

# class MyMixin:
#     def do_a(self):
#         print(self.a)
#
#     def do_b(self, arg1, arg2):
#         print(self.b)
#
#
# class MyClass(MyMixin):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# Ловля ОШИБОК  TRY EXCEPT

# a = int(input('a: '))
# b = int(input('b: '))
#
# try:
#     result = a / b
# except ZeroDivisionError as err:
#     print(f"b это ноль - {err}")
# except Exception as err:
#     print(f"SOMETHING WRONG - {err} !!!")
# else:
#     print('Ошибки небыло.')
# finally:
#     print('Сработает всегда.')

# ВЫЗОВ ОШИБКИ

# a = int(input('a: '))
# b = int(input('b: '))
#
# if b == 0:
#     raise ZeroDivisionError('b это ноль.')

# СОЗДАНИЕ СОБСТВЕННЫХ ОШИБОК

# class MyException(Exception):
#     def __init__(self, message='AAA!!'):
#         super().__init__(message)
#
# raise MyException
