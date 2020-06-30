class MyTime:
    def __init__(self, stroka=None):
        self.stroka = stroka
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        if self.stroka is not None:
            self.stroka = self.stroka.split('-')
            self.hours = self.stroka[0]
            self.minutes = self.stroka[1]
            self.seconds = self.stroka[2]

    def __str__(self):
        return f"{self.hours}-{self.seconds}-{self.minutes}"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ne__(self, other):
        return self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds

    def __add__(self, other):
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds

    def __sub__(self, other):
        self.hours -= other.hours
        self.minutes -= other.minutes
        self.seconds -= other.seconds

    def __gt__(self, other):
        return self.hours > other.hours or self.minutes > other.minutes or self.seconds > other.seconds

    def __lt__(self, other):
        return self.hours < other.hours or self.minutes < other.minutes or self.seconds < other.seconds


a = MyTime()
b = MyTime('2-2-2')
print(a.__str__())

