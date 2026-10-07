from abc import ABC as a, abstractmethod as am


# Abstract Base Class
class Library_item(a):

    @am
    def disp(self):
        pass

    @am
    def get_type(self):
        pass


# Basic Book class
class Book(Library_item):

    total_books = 0

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_available = True
        Book.total_books += 1

    # Encapsulation
    def issue_book(self):
        if self.__is_available:
            self.__is_available = False
            print("Book issued successfully")
        else:
            print("Book is already issued")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print("Book returned successfully")
        else:
            print("Book is already available")

    def is_available(self):
        return self.__is_available

    def disp(self):
        print("Book Id:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Is it available:", self.is_available())

    def get_type(self):
        return "Book"

    # Operator Overloading
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.book_id == other.book_id
        return False

    def __str__(self):
        return f"{self.title} by {self.author}"


# eBook
class Ebook(Book):

    def __init__(self, book_id, title, author, file_size):
        super().__init__(book_id, title, author)
        self.file_size = file_size

    # Method overriding
    def issue_book(self):
        if self.is_available():
            super().issue_book()
            print(f"'{self.title}' eBook access granted")
        else:
            print(f"Access to '{self.title}' already granted")

    # Return eBook / Revoke access
    def return_book(self):
        if not self.is_available():
            super().return_book()
            print(f"Access to '{self.title}' revoked")
        else:
            print(f"No active access for '{self.title}'")

    def get_type(self):
        return "Ebook"

    def disp(self):
        print(
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"File Size: {self.file_size} | "
            f"Available: {self.is_available()}"
        )


# Printed Book
class PrintedBook(Book):

    def __init__(self, book_id, title, author, pages):
        super().__init__(book_id, title, author)
        self.pages = pages

    # Method overriding
    def issue_book(self):
        if self.is_available():
            super().issue_book()
            print(f"Printed book '{self.title}' issued physically")
        else:
            print("Book already issued")

    # Return Printed Book
    def return_book(self):
        if not self.is_available():
            super().return_book()
            print(f"Printed book '{self.title}' returned physically")
        else:
            print("Book is already available")

    def get_type(self):
        return "Printed Book"

    def disp(self):
        super().disp()
        print("Pages:", self.pages)


# Member Class
class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            book.issue_book()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("Book was not borrowed by this member")

    def disp_member(self):
        print("\nMember Id:", self.member_id)
        print("Name:", self.name)
        print("Borrowed books:")

        if not self.borrowed_books:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print("-", book)


# Student Member
class StudentMember(Member):

    def __init__(self, member_id, name, college):
        super().__init__(member_id, name)
        self.college = college

    def disp_member(self):
        super().disp_member()
        print("College:", self.college)


# Faculty Member
class FacultyMember(Member):

    def __init__(self, member_id, name, dept):
        super().__init__(member_id, name)
        self.dept = dept

    def disp_member(self):
        super().disp_member()
        print("Department:", self.dept)


# Library Class
class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully")

    # Remove Book
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book removed successfully")
                return

        print("Book not found")

    # Register Member
    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' added successfully")

    # Search Book
    def search_book(self, title=None, author=None):
        found = False

        for book in self.books:

            if title and title.lower() in book.title.lower():
                book.disp()
                found = True

            elif author and author.lower() in book.author.lower():
                book.disp()
                found = True

        if not found:
            print("No book found")

    # Display Books
    def display_books(self):
        print("\n----- Library Books -----")

        if not self.books:
            print("No books available")
            return

        for book in self.books:
            book.disp()

    # Display Members
    def disp_members(self):
        print("\n----- Members -----")

        if not self.members:
            print("No members registered")
            return

        for member in self.members:
            member.disp_member()

    # Find Member
    def find_memb(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member

        return None

    # Find Book
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book

        return None


# Creating Library
library = Library("ABC Central Library")


# Runtime Menu
while True:

    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Search Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Remove Book")
    print("9. Exit")

    choice = input("Enter your choice: ")


    # Add Book
    if choice == "1":

        print("\n1. Basic Book")
        print("2. Printed Book")
        print("3. eBook")

        book_type = input("Enter book type: ")

        book_id = int(input("Enter book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")

        if book_type == "1":

            book = Book(book_id, title, author)

        elif book_type == "2":

            pages = int(input("Enter number of pages: "))
            book = PrintedBook(book_id, title, author, pages)

        elif book_type == "3":

            file_size = input("Enter file size: ")
            book = Ebook(book_id, title, author, file_size)

        else:
            print("Invalid book type")
            continue

        library.add_book(book)


    # Add Member
    elif choice == "2":

        print("\n1. Student Member")
        print("2. Faculty Member")

        member_type = input("Enter member type: ")

        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")

        if member_type == "1":

            college = input("Enter college: ")
            member = StudentMember(member_id, name, college)

        elif member_type == "2":

            dept = input("Enter department: ")
            member = FacultyMember(member_id, name, dept)

        else:
            print("Invalid member type")
            continue

        library.register_member(member)


    # Display Books
    elif choice == "3":

        library.display_books()


    # Display Members
    elif choice == "4":

        library.disp_members()


    # Search Book
    elif choice == "5":

        print("\n1. Search by Title")
        print("2. Search by Author")

        search_choice = input("Enter choice: ")

        if search_choice == "1":

            title = input("Enter title: ")
            library.search_book(title=title)

        elif search_choice == "2":

            author = input("Enter author: ")
            library.search_book(author=author)

        else:
            print("Invalid choice")


    # Borrow Book
    elif choice == "6":

        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))

        member = library.find_memb(member_id)
        book = library.find_book(book_id)

        if member is None:
            print("Member not found")

        elif book is None:
            print("Book not found")

        else:
            member.borrow_book(book)


    # Return Book
    elif choice == "7":

        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))

        member = library.find_memb(member_id)
        book = library.find_book(book_id)

        if member is None:
            print("Member not found")

        elif book is None:
            print("Book not found")

        else:
            member.return_book(book)


    # Remove Book
    elif choice == "8":

        book_id = int(input("Enter book ID: "))
        library.remove_book(book_id)


    # Exit
    elif choice == "9":

        print("Thank you for using the Library Management System")
        break


    else:

        print("Invalid choice. Please try again.")