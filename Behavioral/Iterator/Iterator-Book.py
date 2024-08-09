# Class Book represent the items in the collection
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


# BookCollection class hold our Book objects and implement the __iter__() method to return an iterator.
class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        return BookIterator(self.books)


# BookIterator class implements the iterator interface and define how the BookCollection can be iterated.
class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration


# Usage
books_collection = BookCollection()
books_collection.add_book(Book('Sahih al-Bukhari', 'Imam Muhammad al-Bukhari'))
books_collection.add_book(Book('Ihya Ulum al-Din', 'Imam Abu Hamid al-Ghazali'))
books_collection.add_book(Book('Al-Muwatta', 'Imam Malik ibn Anas'))

# Iterate over the collection using a for loop
for book in books_collection:
    print(book)
