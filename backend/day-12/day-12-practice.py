# Creating a class
class Programmer:
    # Declaring constructors
    def __init__(self, name, age, department, skill):
        self.name = name
        self.age = age
        self.department = department
        self.skill = skill
        
    
    # Adding methods
    def skills(self, new_skill):
        self.skill.append(new_skill)
        

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")
        if len(self.skill) > 0:
            print("Skill:")
            for skill in self.skill:
                print(skill)
        else:
            print("Skill: None yet")
            

# Prompt the user for information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
department = input("Enter your department: ")
skill = input("Enter your skill/s: ").split

# Instantiating objects
programmer1 = Programmer(name, age, department, skill)

# Using methods
programmer1.skills("Python")
programmer1.show()
