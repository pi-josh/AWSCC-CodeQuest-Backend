# FizzBuzz

# Prompt the user a limit for the range of numbers
num = int(input("Limit: "))

# For loop
for i in range(num):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        print("FizzBuzz!")
    elif (i + 1) % 3 == 0:
        print("Fizz")
    elif (i + 1) % 5 == 0:
        print("Buzz")
    else:
        print(i + 1)
