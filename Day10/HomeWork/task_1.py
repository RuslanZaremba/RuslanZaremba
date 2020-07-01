# class MyTime:
#     def __init__(self, hours=None, minutes=None, seconds=None):
#         self.hours = hours or 0
#         self.minutes = minutes or 0
#         self.seconds = seconds or 0
#         self.string = None
#         if self.hours is not None and type(self.hours) is str:
#             self.string = list(map(int, self.hours.split('-')))
#             for i in range(len(self.string))[::-1]:
#                 if self.string[i] > 59:
#                     self.string[i - 1] += self.string[i] // 60
#                     self.string[i] = self.string[i] % 60
#
#             self.hours = self.string[0]
#             self.minutes = self.string[1]
#             self.seconds = self.string[2]
#         return f"{self.hours}"
#
#     def __str__(self):
#         return f"{self.hours}-{self.minutes}-{self.seconds}"
#
#
# a = MyTime(1, 1, 1)
# print(a)
# b = MyTime(a)
# print(b)


class MyTime:
    def __init__(self, hours=None, minutes=None, seconds=None):
        self.hours = hours or 0
        self.minutes = minutes or 0
        self.seconds = seconds or 0
        self.string = None
        if self.hours is not None and type(self.hours) is str:
            self.string = list(map(int, self.hours.split('-')))
            for i in range(len(self.string))[::-1]:
                if self.string[i] > 59:
                    self.string[i - 1] += self.string[i] // 60
                    self.string[i] = self.string[i] % 60

            self.hours = self.string[0]
            self.minutes = self.string[1]
            self.seconds = self.string[2]

    def __str__(self):
        return f"{self.hours}-{self.minutes}-{self.seconds}"

b = MyTime(2,3,4)
a = MyTime(b)
print(a)
b = MyTime(a)
print(b)