class Product:
    discount = 10   # static/class variable (10% discount)

    # Constructor (parameterized + parameterless)
    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Method to apply discount
    def apply_discount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        return discounted_price

    # Show product details
    def ShowProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Price after", Product.discount, "% discount:", self.apply_discount())
        print()

    # Destructor
    def __del__(self):
        print("Destructor called for Product ID:", self.pid)


# Creating objects
p1 = Product()  # parameterless constructor
p2 = Product(101, "Laptop", 50000, 2)  # parameterized constructor

# Display product details
p1.ShowProduct()
p2.ShowProduct()