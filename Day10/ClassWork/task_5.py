class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


my_time_inp=MyTime(input('Введите время: '))
my_time = MyTime()
print(my_time.hours)
