class Library:
    def __init__(self, name, autor, year):
        self.name = name
        self.autor = autor
        self.year = year
        self.archive = []

    def add(self, **kwargs):
        for i in kwargs:
            self.archive.append({
                'name': self.name,
                'autor': self.autor,
                'year': self.year
            })

    @property
    def get_archive(self):
        return self.archive
book = Library('Mtsiri', 'Pushkin', 1899)
book.add()
print(book.get_archive)

