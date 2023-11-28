# name of file: main.py
from circle_area import calculate_area

# Prompt the user for the radius
radius = int(input("Enter the radius: "))

# Calculate the area using the module
area = calculate_area(radius)

# Display the result
print(f"The area of the circle is {area}")
