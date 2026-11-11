class Book:
    count = 0   # static/class variable

    # Constructor (supports parameterized and parameterless)
    def __init__(self, bid=0, bname="Unknown", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1   # increase count when object is created

    # ShowBook method
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        print()

    # Destructor
    def __del__(self):
        print("Destructor called for Book ID:", self.bid)


# Creating objects
b1 = Book()   # parameterless constructor
b2 = Book(101, "Python Programming", 500, "Guido van Rossum")

# Display book details
b1.ShowBook()
b2.ShowBook()

# Display total objects created
print("Total objects created:", Book.count)