class Information:
    def __init__(self):
        self._address = 'Minsk'

    @property
    def address(self):
        return self._adress

    @address.setter
    def address(self, sity):
        self._address = sity

info = Information()

print(info._address)
info.address = 'Gomel'
print(info._address)