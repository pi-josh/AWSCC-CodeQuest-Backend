# Implementing two of the pillars of OOP: Abstraction and Inheritance

# Abstraction
class Square():
    def perimeter(self, side):
        return side * 4
    
# Getting the perimeter of a square using class Square
square = Square()
result = square.perimeter(5)
print("Perimeter of the square using class Square:", result)


# Inheritance
class AreaSquare(Square):
    def area(self, side):
        return side ** 2

# Getting the perimeter and area of a square using class AreaSquare
square = AreaSquare()
perimeter = square.perimeter(5)
area = square.area(5)

print("Perimeter of the square using class AreaSquare:", perimeter)
print("Area of the square using class AreaSquare:", area)
