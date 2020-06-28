class Library:
    def __init__(self, **kwargs):
        self.data = [i[1] for i in kwargs.items()]

    def add(self, **kwargs):
        self.data.extend([i[1] for i in kwargs.items()])

    def find(self, val):
        data_for_find = []
        for i in self.data:
            if val in i.values():
                data_for_find.append(i)
        return data_for_find

    def deleter(self, value):
        for i in self.find(value):
            if i in self.data:
                self.data.remove(i)

    def sort(self, field):
        return self.data.sort(field)


book = Library(
    first={'name': 'Mtsiri', 'autor': 'Pushkin', 'genre': 'story', 'date': 1900},
    second={'name': 'Mumu', 'autor': 'Tolstoi', 'genre': 'story', 'date': 1905}
)
book.add(sec={'name': 'Mother', 'autor': 'Esenin', 'genre': 'poem', 'date': 1895})
# print(book.data)
print(book.find(1900))
# book.deleter('Mumu')
print(book.data)

