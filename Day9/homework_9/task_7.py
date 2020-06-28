class Information:
    def __init__(self):
        self._address = 'Minsk'
        self.param = {'Minsk': 'RB', 'Moscow': 'Russia'}

    @property
    def address(self):
        for k, v in self.param.items():
            if self._address in k:
                return self._address + ' ' + self.param.get(k)

    @address.setter
    def address(self, sity):
        self._address = sity



info = Information()

print(info._address)
info.address = 'Gomel'
print(info._address)
