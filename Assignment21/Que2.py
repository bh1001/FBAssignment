class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def get_data(self):
        try:
            self.model_number = int(input("Enter Model Number: "))
            if self.model_number > 9999:
                raise Exception("Model number cannot have more than 4 digits.")

            self.screen_size = int(input("Enter Screen Size (in inches): "))
            if self.screen_size < 12 or self.screen_size > 70:
                raise Exception("Screen size must be between 12 and 70 inches.")

            self.price = float(input("Enter Price (Rs): "))
            if self.price < 0 or self.price > 5000:
                raise Exception("Price must be between 0 and 5000 Rs.")

        except Exception as e:
            print("Exception caught:", e)
            print("Resetting all values to 0.")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("\nTelevision Details")
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size, "inches")
        print("Price: Rs", self.price)


# main function
def main():
    tv = Television()
    tv.get_data()
    tv.display()


# program execution
main()