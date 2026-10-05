# Author: Alonso Bernal
# Week 6 Programming Assignment
# Library Book Management System
# Base level

class Book:

    #Initalize new book object
    def __init__(self, title, author, isbn, year, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre

        self.available = True
        self.borrower = None

    #Returns availability status of the book
    def get_status(self):
        if self.available:
            return "Available"
        else:
            return f"Checked out to {self.borrower}"
    #Returns the book information as a string
    def __str__(self):
        return (
            f"{self.isbn:<17} "
            f"{self.title:<22} "
            f"by {self.author:<16} "
            f"{self.year:<6} "
            f"{self.genre:<16} "
            f"{self.get_status()}"
        )
    #attempts to check out the book to a borrower
    def check_out(self, patron_name):
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        else:
            return False
    #Returns the book to the library
    def return_book(self):
        self.available = True
        self.borrower = None

        return f"'{self.title}' has been returned and is now available."

collection = [
    Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "978-0590353427", 1997, "Fantasy"),
    Book("The Hunger Games", "Suzanne Collins", "978-0439023481", 2008, "Dystopian Fiction"),
    Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1960, "Classic Fiction"),
    Book("The Shining", "Stephen King", "978-0307743657", 1977, "Horror"),
    Book("The Da Vinci Code", "Dan Brown", "978-0307474278", 2003, "Mystery"),
    Book("The Fault in Our Stars", "John Green", "978-0525478812", 2012, "Young Adult")
]
print("=== Full Collection ===")

for book in collection:
    print(book)

print("\n=== Checking Out Books ===")

if collection[0].check_out("Alonso"):
    print(f"{collection[0].title} was checked out successfully.")

if collection[1].check_out("Jackie"):
    print(f"{collection[1].title} was checked out successfully.")

print("\n=== Updated Collection ===")

for book in collection:
    print(book)
print("\n=== Attempting Second Checkout ===")

if collection[0].check_out("Michael"):
    print(f"{collection[0].title} was checked out successfully.")
else:
    print(f"{collection[0].title} is already checked out.")

print("\n=== Returning a Book ===")

print(collection[1].return_book())

print("\n=== Collection After Return ===")

for book in collection:
    print(book)

print("\n=== Books Sorted by Title ===")

sorted_books = sorted(collection, key=lambda book: book.title)

for book in sorted_books:
    print(book)

print("\n=== Available Books ===")

available_books = [book for book in collection if book.available]

for book in available_books:
    print(book)
        