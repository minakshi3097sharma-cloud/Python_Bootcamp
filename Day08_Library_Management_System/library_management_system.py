print("=" * 55)
print("        LIBRARY MANAGEMENT SYSTEM")
print("=" * 55)


# ---------------------- Book Class ----------------------

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.title} | {self.author} | {status}")


# ---------------------- Library Class ----------------------

class Library:

    def __init__(self):
        self.books = []

    def add_book(self):

        title = input("\nEnter Book Title : ")
        author = input("Enter Author Name: ")

        book = Book(title, author)
        self.books.append(book)

        print("\nBook added successfully!")

    def view_books(self):

        if not self.books:
            print("\nNo books available.")
            return

        print("\n")
        print("-" * 55)
        print("Title | Author | Status")
        print("-" * 55)

        for book in self.books:
            book.display()

    def borrow_book(self):

        title = input("\nEnter Book Title: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    print("\nBook borrowed successfully!")

                else:
                    print("\nBook is already borrowed.")

                return

        print("\nBook not found.")

    def return_book(self):

        title = input("\nEnter Book Title: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.available:
                    book.available = True
                    print("\nBook returned successfully!")

                else:
                    print("\nBook is already available.")

                return

        print("\nBook not found.")


# ---------------------- Inheritance ----------------------

class DigitalLibrary(Library):

    def library_type(self):
        print("\nThis is a Digital Library.")


# ---------------------- Polymorphism ----------------------

class LibraryInfo:

    def show(self):
        print("Welcome to Library")


class StudentLibrary(LibraryInfo):

    def show(self):
        print("Welcome to Student Library")


# ---------------------- Main Program ----------------------

library = DigitalLibrary()

student = StudentLibrary()
student.show()

while True:

    print("\n" + "=" * 55)
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Library Type")
    print("6. Exit")
    print("=" * 55)

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.library_type()

    elif choice == "6":
        print("\nThank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")