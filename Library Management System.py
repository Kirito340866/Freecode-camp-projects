class Book:
	def __init__(self,title,author,is_borrowed=False):
		self.title = title
		self.author = author
		self.is_borrowed = is_borrowed
	def display_info(self):
		if self.is_borrowed:
			print(f"Book: {self.title} is Borrowed")
		if not self.is_borrowed:
			print(f"Book: {self.title} is Not Borrowed yet")

class Member:
	def __init__(self,name):
		self.name = name
		self.borrow_books = []
	def borrow_book(self,book):
		self.borrow_books.append(book)
		book.is_borrowed = True
		print(f"Member: {self.name} Borrowed Book: {book.title} by {book.author}")
	def return_book(self,book):
		if not book in self.borrow_books:
			print(f"The book: {book.title} is not borrowed")
			return
		book.is_borrowed = False
		self.borrow_books.remove(book)
		print(f"Member: {self.name} returned Book: {book.title}")
	def show_borrowed_books(self):
		if len(self.borrow_books) == 0:
			return
		print("\n--- Borrowed Book ---\n")
		for book in self.borrow_books:
			print(f"Book: {book.title} | Author: {book.author}")

class Library:
	def __init__(self,name):
		self.name = name
		self.books = []
		self.members = []
	def add_book(self,book):
		self.books.append(book)
	def register_member(self,member):
		self.members.append(member)
	def show_library_books(self):
		for book in self.books:
			print(f"Book: {book.title} | Author: {book.author}")
	def lend_book(self,member,book):
		if not book in self.books:
			print(f"Book: {book.title} is not found in Library")
			return
		if not member in self.members:
			print(f"This user is not in Member")
			return
		if book.is_borrowed:
			print("This book is already borrowed")
			return
		member.borrow_book(book)
	def return_book(self,member,book):
		member.return_book(book)


book1 = Book("The quiet life","IDK")
book2 = Book("Python","Saturn")
book3 = Book("Java","Saturn")


member1 = Member("Kirito")
member2 = Member("Alice")

library = Library("Star")

member1.borrow_book(book1)
book1.display_info()

library.add_book(book1)
library.add_book(book2)
library.register_member(member1)
library.show_library_books()
library.lend_book(member1,book1)
library.lend_book(member2,book2)
library.lend_book(member1,book3)
library.return_book(member1,book1)
library.lend_book(member1,book1)
member1.show_borrowed_books()
