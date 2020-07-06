class A:
    def do_something(self):
        print('AAA')
class B(A):
    def do_something(self):
        super().do_something()
        print('BBB')

b=B()
b.do_something()
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def ae(self):
#         print(self.a)


# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#
#     def sum(self):
#         print(self.b + self.a)
#
# a = A(1)
# a.ae()
# b = B(12, 12)
# b.sum()
# class Car:
#     last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.last_model = model
#
#
# car1 = Car('Audi')
# print(Car.last_model)
# car2 = Car('BMW')
# print(Car.last_model)
# print(car1.last_model)
# print(car2.last_model)
