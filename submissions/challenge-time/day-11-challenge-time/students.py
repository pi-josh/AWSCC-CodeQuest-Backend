# A program that reads and sorts name alphabetically in a text file

# Variable to store the sorted list of names
sorted_names = []

# Reading the text file
with open('students.txt', 'r') as file:
    lines = sorted(file.readlines())
    for line in lines:
        sorted_names.append(line)

# Writing into the text file
with open('students_sorted.txt', 'w') as file:
    for name in sorted_names:
        file.writelines(name)
