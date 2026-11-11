class Product:
    # Constructor (supports parameterized and parameterless)
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor called")

    # Method to display product details
    def ShowProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # Destructor
    def __del__(self):
        print("Destructor called. Product object deleted.")


# Using parameterless constructor
p1 = Product()
p1.pid = 1
p1.pname = "Laptop"
p1.price = 50000
p1.quantity = 2

print("\nProduct Details:")
p1.ShowProduct()

# Using parameterized constructor
p2 = Product(2, "Mobile", 20000, 5)

print("\nProduct Details:")
p2.ShowProduct()