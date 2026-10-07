# from abc import ABC as a, abstractmethod as am


# # Abstract Base Class
# class Library_item(a):

#     @am
#     def disp(self):
#         pass

#     @am
#     def get_type(self):
#         pass


# # Basic Book class
# class Book(Library_item):

#     total_books = 0

#     def __init__(self, book_id, title, author):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.__is_available = True
#         Book.total_books += 1

#     # Encapsulation
#     def issue_book(self):
#         if self.__is_available:
#             self.__is_available = False
#             print("Book issued successfully")
#         else:
#             print("Book is already issued")

#     def return_book(self):
#         self.__is_available = True
#         print("Book returned successfully")

#     def is_available(self):
#         return self.__is_available

#     def disp(self):
#         print("Book Id:", self.book_id)
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Is it available:", self.is_available())

#     def get_type(self):
#         return "Book"

#     # Operator Overloading
#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.book_id == other.book_id
#         return False

#     def __str__(self):
#         return f"{self.title} by {self.author}"


# # eBook
# class Ebook(Book):

#     def __init__(self, book_id, title, author, file_size):
#         super().__init__(book_id, title, author)
#         self.file_size = file_size
#         self.__has_access = False

#     # Method overriding
#     def issue_book(self):
#         if not self.__has_access:
#             self.__has_access = True
#             print(f"'{self.title}' eBook access granted")
#         else:
#             print(f"Access to '{self.title}' already granted")

#     # Revoke eBook access
#     def revoke_access(self):
#         if self.__has_access:
#             self.__has_access = False
#             print(f"Access to '{self.title}' revoked")
#         else:
#             print(f"No active access for '{self.title}'")

#     def is_available(self):
#         return not self.__has_access

#     def get_type(self):
#         return "Ebook"

#     def disp(self):
#         print(
#             f"ID: {self.book_id} | "
#             f"Title: {self.title} | "
#             f"Author: {self.author} | "
#             f"File Size: {self.file_size} | "
#             f"Access: {self.__has_access}"
#         )


# # Printed Book
# class PrintedBook(Book):

#     def __init__(self, book_id, title, author, pages):
#         super().__init__(book_id, title, author)
#         self.pages = pages

#     # Method overriding
#     def issue_book(self):
#         if self.is_available():
#             print(f"Printed book '{self.title}' issued physically")
#             super().issue_book()
#         else:
#             print("Book already issued")

#     def get_type(self):
#         return "Printed Book"

#     def disp(self):
#         super().disp()
#         print("Pages:", self.pages)


# # Member Class
# class Member:

#     def __init__(self, member_id, name):
#         self.member_id = member_id
#         self.name = name
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         if book.is_available():
#             book.issue_book()
#             self.borrowed_books.append(book)
#             print(f"{self.name} borrowed {book.title}")
#         else:
#             print(f"{book.title} not available")

#     def return_book(self, book):
#         if book in self.borrowed_books:
#             book.return_book()
#             self.borrowed_books.remove(book)
#             print(f"{self.name} returned {book.title}")
#         else:
#             print("Book was not borrowed by this member")

#     def disp_member(self):
#         print("\nMember Id:", self.member_id)
#         print("Name:", self.name)
#         print("Borrowed books:")

#         if not self.borrowed_books:
#             print("No books borrowed")
#         else:
#             for book in self.borrowed_books:
#                 print("-", book)


# # Student Member
# class StudentMember(Member):

#     def __init__(self, member_id, name, college):
#         super().__init__(member_id, name)
#         self.college = college

#     def disp_member(self):
#         super().disp_member()
#         print("College:", self.college)


# # Faculty Member
# class FacultyMember(Member):

#     def __init__(self, member_id, name, dept):
#         super().__init__(member_id, name)
#         self.dept = dept

#     def disp_member(self):
#         super().disp_member()
#         print("Department:", self.dept)


# # Library Class
# class Library:

#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.members = []

#     # Add book
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Book '{book.title}' added successfully")

#     # Remove book
#     def remove_book(self, book_id):
#         for book in self.books:
#             if book.book_id == book_id:
#                 self.books.remove(book)
#                 print("Book removed successfully")
#                 return

#         print("Book not found")

#     # Register member
#     def register_member(self, member):
#         self.members.append(member)
#         print(f"Member '{member.name}' added successfully")

#     # Search book
#     def search_book(self, title=None, author=None):
#         found = False

#         for book in self.books:

#             if title and title.lower() in book.title.lower():
#                 book.disp()
#                 found = True

#             elif author and author.lower() in book.author.lower():
#                 book.disp()
#                 found = True

#         if not found:
#             print("No book found")

#     # Display books
#     def display_books(self):
#         print("\n----- Library Books -----")

#         if not self.books:
#             print("No books available")
#             return

#         for book in self.books:
#             book.disp()

#     # Display members
#     def disp_members(self):
#         print("\n----- Members -----")

#         for member in self.members:
#             member.disp_member()

#     # Find member
#     def find_memb(self, member_id):
#         for member in self.members:
#             if member.member_id == member_id:
#                 return member

#         return None

#     # Find book
#     def find_book(self, book_id):
#         for book in self.books:
#             if book.book_id == book_id:
#                 return book

#         return None


# # Creating Library
# library = Library("ABC Central Library")


# # Creating Books
# book1 = Book(101, "Python", "Shiva")
# book2 = PrintedBook(102, "Java", "Van", 500)
# book3 = Ebook(103, "ML", "Rossum", "10MB")


# # Adding Books
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)


# # Creating members
# student = StudentMember(1, "Saran", "MRCET")
# faculty = FacultyMember(2, "Dr. Kamal", "CSE")


# # Adding Members
# library.register_member(student)
# library.register_member(faculty)


# # Display Books
# library.display_books()


# # Borrow normal book
# student.borrow_book(book1)

# student.disp_member()

# student.return_book(book1)


# # Search books
# library.search_book(title="Python")
# library.search_book(author="rossum")


# # eBook access
# book3.issue_book()

# # Try to give access again
# book3.issue_book()

# # Revoke eBook access
# book3.revoke_access()

# # Try to revoke again
# book3.revoke_access()

# # Display eBook
# book3.disp()









from abc import ABC, abstractmethod as am
class Library_item(ABC):
    @am
    def disp(self):
        pass
    @am
    def get_type(self):
        pass

class Book(Library_item) :
    total_books = 0
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.__is_available = True
        Book.total_books += 0
    def 