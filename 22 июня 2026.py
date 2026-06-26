class Book:
    def __init__(self, title, author, publisher, pages):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages

    def show(self):
        print("Название: " + self.title)
        print("Автор: " + self.author)
        print("Издательство: " + self.publisher)
        print("Страниц: " + str(self.pages))


def show_books(books):
    for i in range(len(books)):
        print("Книга", i+1)
        books[i].show()
        print()


book1 = Book("Мастер и Маргарита", "Булгаков", "Азбука", 480)
book2 = Book("Война и мир", "Толстой", "Наука", 1274)
book3 = Book("1984", "Оруэлл", "АСТ", 320)

books = [book1, book2, book3]
