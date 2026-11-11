class ComplexNumber:
    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Operator overloading for +
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return ComplexNumber(r, i)

    # Operator overloading for -
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return ComplexNumber(r, i)

    # Display complex number
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Destructor
    def __del__(self):
        print("ComplexNumber object destroyed")


# Creating objects
c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, 3)

# Using overloaded operators
c3 = c1 + c2
c4 = c1 - c2

print("First Complex Number:", c1)
print("Second Complex Number:", c2)
print("Addition:", c3)
print("Subtraction:", c4)