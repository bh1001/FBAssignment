class Shirt:
    increment = 0.10   # static variable (10% increase)

    # Constructor (parameterized + parameterless)
    def __init__(self, sid=0, sname="Unknown", type="Unknown", price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Method to calculate price according to size
    def calculate_price(self):
        if self.size.lower() == "small":
            return self.price
        elif self.size.lower() == "medium":
            return self.price + (self.price * Shirt.increment)
        elif self.size.lower() == "large":
            return self.price + (self.price * 2 * Shirt.increment)
        elif self.size.lower() == "xlarge":
            return self.price + (self.price * 3 * Shirt.increment)
        else:
            return self.price

    # ShowShirt method
    def ShowShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Base Price:", self.price)
        print("Size:", self.size)
        print("Final Price:", self.calculate_price())
        print()

    # Destructor
    def __del__(self):
        print("Destructor called for Shirt ID:", self.sid)


# Creating objects
s1 = Shirt()
s2 = Shirt(101, "Office Wear", "Formal", 1000, "large")

# Display details
s1.ShowShirt()
s2.ShowShirt()