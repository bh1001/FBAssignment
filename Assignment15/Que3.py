class Shirt:
    # Constructor (supports parameterized and parameterless)
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Constructor called")

    # Method to display shirt details
    def ShowShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)

    # Destructor
    def __del__(self):
        print("Destructor called. Shirt object deleted.")


# Using parameterless constructor
s1 = Shirt()
s1.sid = 1
s1.sname = "Cotton Shirt"
s1.type = "Formal"
s1.price = 1200
s1.size = "Large"

print("\nShirt Details:")
s1.ShowShirt()

# Using parameterized constructor
s2 = Shirt(2, "Denim Shirt", "Casual", 1500, "Medium")

print("\nShirt Details:")
s2.ShowShirt()