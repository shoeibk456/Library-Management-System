class Book:
    def __init__(self, book_name, writer, publish_year):
        self.book_name = book_name
        self.writer = writer
        self.publish_year = publish_year
        self.status = "Available"

    # book details
    def show_details(self):
        print("Book Information")
        print("Book Name:", self.book_name)
        print("Writer:", self.writer)
        print("Publish Year:", self.publish_year)
        print("Status:", self.status)


# Patron Class
class Patron:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id
        self.borrowed = []

    def take_book(self, book):
        self.borrowed.append(book.book_name)
        print(self.student_name, "borrowed", book.book_name)


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.book_list = []
        self.patron_list = []

    # Add books
    def insert_book(self, book):
        self.book_list.append(book)
        print(book.book_name, "added in library")

    # Register patrons
    def add_patron(self, patron):
        self.patron_list.append(patron)
        print(patron.student_name, "registered successfully")

    # Issue book
    def issue_book(self, book, patron):
        if book.status == "Available":
            book.status = "Borrowed"
            patron.take_book(book)
        else:
            print("Book already borrowed")

library1 = Library("Smart Library")

# Creating Book Objects
book1 = Book("Python Programming", "Mahim", 2018)
book2 = Book("Computer Basics", "Ethan", 2019)

patron1 = Patron("Shoeib", 201)

# Adding books to library
library1.insert_book(book1)
library1.insert_book(book2)


library1.add_patron(patron1)
library1.issue_book(book1, patron1)

# Displaying book details
book1.show_details()

# Display borrowed books
print("Borrowed Books:", patron1.borrowed)
