# Program that evaluates whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))

if num < 0:
    print(f"{num} is a Negative number!")
elif num > 0:
    print(f"{num} is a Positive number!")
else:
    print("That number is a Zero!")
