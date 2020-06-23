class Private:
    def __init__(self):
        self._master = 'Master'

    def out(self):
        return self._master


private = Private()
print(private.out())
