class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"


book1 = Book("Moby-Dick", "Herman Melville", 1851)
book2 = Book("DRACULA","Bram Stoker", 1897)
book3 = Book("Frankenstein", "Mary Shelley ", 1818)


print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
