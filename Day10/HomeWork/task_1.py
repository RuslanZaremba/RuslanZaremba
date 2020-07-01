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
            # if self.string[2] > 59:
            #     self.string[1] += self.string[2] // 60
            #     self.string[2] = self.string[2] % 60
            # if self.string[1] > 59:
            #     self.string[0] += self.string[1] // 60
            #     self.string[1] = self.string[1] % 60
            self.hours = self.string[0]
            self.minutes = self.string[1]
            self.seconds = self.string[2]

    def __str__(self):
        return f"{self.hours}-{self.minutes}-{self.seconds}"

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


a = MyTime(1, 1, 1)
print(a.)
