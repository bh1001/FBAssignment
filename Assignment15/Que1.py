class Book:
    # Constructor (works as parameterized and parameterless)
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Constructor called")

    # Method to display book details
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    # Destructor
    def __del__(self):
        print("Destructor called. Book object deleted.")


# Parameterless constructor
b1 = Book()
b1.bid = 101
b1.bname = "Python Programming"
b1.price = 450
b1.author = "John Smith"
print("\nBook Details:")
b1.ShowBook()

# Parameterized constructor
b2 = Book(102, "Data Structures", 550, "Mark Allen")
print("\nBook Details:")
b2.ShowBook()