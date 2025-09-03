class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def display_info(self):
        print("Book Information:")
        print(f"Book title: {self.title}, Book author: {self.author}, Book isbn: {self.isbn}")

b = Book("The Grass is Always Greener","Jeffrey Archer","1-86092-049-7")
b.display_info()
        
    
    