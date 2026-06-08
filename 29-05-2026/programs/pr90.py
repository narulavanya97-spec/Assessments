class Shape:
    def __init__(self):
        pass  # Default constructor

    def area(self):
        return 0  # Shape's area is 0 by default


class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Call the parent class constructor
        self.length = length

    def area(self):
        return self.length ** 2  # Calculate the area of the square


# Example usage
square = Square(5)
print("Area of square:", square.area())

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


# Create instances of the classes
shape = Shape()
square = Square(float(input("Enter the side length of the square: ")))

# Calculate and print the areas
print("Shape's area by default:", shape.area())
print("Area of the square:", square.area())


