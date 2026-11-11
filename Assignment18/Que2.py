class Distance:
    # Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    # Normalize distance values
    def normalize(self):
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm = self.cm % 100
        if self.m >= 1000:
            self.km += self.m // 1000
            self.m = self.m % 1000

    # Overload + operator
    def __add__(self, other):
        k = self.km + other.km
        m = self.m + other.m
        c = self.cm + other.cm
        result = Distance(k, m, c)
        result.normalize()
        return result

    # Overload - operator
    def __sub__(self, other):
        total1 = self.km*100000 + self.m*100 + self.cm
        total2 = other.km*100000 + other.m*100 + other.cm
        diff = abs(total1 - total2)

        k = diff // 100000
        diff %= 100000
        m = diff // 100
        c = diff % 100

        return Distance(k, m, c)

    # Display distance
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    # Destructor
    def __del__(self):
        print("Distance object destroyed")


# Creating objects
d1 = Distance(2, 500, 80)
d2 = Distance(1, 600, 50)

# Operator overloading
d3 = d1 + d2
d4 = d1 - d2

print("Distance 1:", d1)
print("Distance 2:", d2)
print("Addition:", d3)
print("Subtraction:", d4)