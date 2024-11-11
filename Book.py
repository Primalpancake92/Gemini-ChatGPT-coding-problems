class Book: 
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    
    def borrow(self) -> str:
        if self.available:
            self.available = False
            return "Book is now borrowed.\n"
        return "Book has already been borrowed.\n"
    

    def return_book(self) -> str:
        if not self.available:
            self.available = True
            return "Book is now returned.\n"
        return "Book has already been returned.\n"
    

class Member: 
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        
    
    def user_borrow_book(self, book : Book):
        print(book.borrow())
        

    def user_return_book(self, book : Book):
        print(book.return_book())
            

class Library: 
    def __init__(self):
        """This class just stores a collection of book objects that belongs 
        to each member of the library collection. This only stores the list
        of books associated with each member.
        """
        self.library = []
        self.member = []
    
    
    def add_book(self, book : Book):
        self.library.append(book)
    
    
    def add_member(self, member : Member):
        self.member.append(member)
        
        
    def list_books(self):
        for book in self.library:
            print(f"Book Title: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.isbn}\n")
    
    
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
    book2 = Book("1984", "George Orwell", "67890")

    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_member(member1)
    library.add_member(member2)

    # List all books
    library.list_books()

    # Member borrows a book
    member1.user_borrow_book(book1)

    # List books again after borrowing
    library.list_books()

    # Member returns the book
    member1.user_return_book(book1)

    # List books again after returning
    library.list_books()