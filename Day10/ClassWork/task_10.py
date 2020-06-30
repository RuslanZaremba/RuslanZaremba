class Book:
    def __init__(self, maker, cost, year, list_count):
        try:
            if maker is not str:
                self.maker = maker
        except TypeError as err:
            print(f"Maker должно быть стр.")
        self.cost = float(cost)
        self.year = int(year)
        self.list_count = int(list_count)


book = Book(21, 21, 1902, 402)
print(type(book.maker))
