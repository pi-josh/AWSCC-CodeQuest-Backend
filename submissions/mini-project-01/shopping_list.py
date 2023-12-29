# Mini Project: Basic Shopping List Program in Python

# Variable to store the items
shopping_list = []

def main():
    welcome()
    menu()
    thank_you()

# Function for reading and writing file to always update the shopping list global variable.
def reading_file():
    global shopping_list
    shopping_list = []
    with open('shopping_list.txt', 'r') as file:
        items = file.readlines()
        for item in items:
            item = item.strip()
            shopping_list.append(item)
            

def writing_file(product):
    with open('shopping_list.txt', 'w') as file:
        for item in shopping_list:
            if product == item:
                print(f"\n\n\t\t\t\t{item} has been removed from your shopping list.\n\n")
                continue
            else:
                file.write(item + "\n")
            

def add_items():
    # Prompt the user for the item to be added
    item = input("Enter the item you want to add: ").lower().capitalize()
    with open('shopping_list.txt', 'a') as file:
        if not item in shopping_list:
            file.write(item + "\n")    
            print(f"\n\n\t\t\t\t{item} has been added to your shopping list.\n\n")
        else:
            print("\n\n\t\t\t\tItem is already on the list!\n\n")

    
def view_items():
    # Show the user the list
    reading_file()
    print("\n\n\t\t\t\tYour shopping list:")
    for item in shopping_list:
        print("\t\t\t\t" + item)
    print("\n\n")


def remove_items():
    # Prompt the user for the item to be removed
    item = input("Enter the item you want to remove: ").lower().capitalize()
    if item in shopping_list:
        writing_file(item)
    else:
        print(f"\n\n\t\t\t\t{item} is not in your shopping list.\n\n")
        

# Function to show the menu to the user
def menu():
    while True:
        # Show the choices on the prompt
        print("""
          Menu.
            1. Add item to the shopping list
            2. View shopping list
            3. Remove item from the shopping list
            4. Quit
          """)
    
        # Prompt the user for their choice
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            add_items()
        elif choice == '2':
            view_items()
        elif choice == '3':
            remove_items()
        elif choice == '4':
            return
        else:
            print("\n\n\t\t\tInvalid input! Please try again...\n\n")


# To welcome the customer
def welcome():
    print("""
        ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
        ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
        ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
        ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
        ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
         ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              
          """)
    print("\t\t\t\tEnjoy shopping!!!\n\n")

# To thank the customer for using the service
def thank_you():
    print("""
        ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
        ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
           ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
           ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
           ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝                                          
          """)
    print("\t\t\t\tPlease come again!!!\n\n")


# Call the main to start the program
main()
