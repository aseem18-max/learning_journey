class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []
    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)
    def showInfo(self):
        print(f"\n\nThe Number of Books in the Library is {self.no_of_books}")
        print(f"Books are :- {self.books}")

l1 = Library()
while True:
    s = input("New Book Added or not :- ")
    if s == 'Yes':
        print("Enter the name of the book :- ")
        new_book = input()
        l1.addBook(new_book)
    else:
        break
l1.showInfo()