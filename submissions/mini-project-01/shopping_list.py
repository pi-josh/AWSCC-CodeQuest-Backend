# Mini Project: Basic Shopping List Program in Python

# Reading the shopping list text file
shopping_list = open('shopping_list.txt', 'r')

def main():
    # Signboard
    print("""
        ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
        ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
        ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
        ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
        ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
         ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              
          """)
    print("\t\t\t\tEnjoy shopping!!!\n\n")
    
    quit = False
    while not quit:
        # Show the menu in the prompt
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
            quit = True
            print("""
        ████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗
        ╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
           ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║
           ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║
           ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝
           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝                                          
          """)
            print("\t\t\t\tPlease come again!!!\n\n")
            shopping_list.close()
        else:
            print("\n\n\t\t\tInvalid input! Please try again...\n\n")


def add_items():
    # Prompt the user for the item to be added
    item = input("Enter the item you want to add: ").lower().capitalize()
    with open('shopping_list.txt', 'a') as file:
        if not item in shopping_list.readlines():
            file.write(item + "\n")    
            print(f"\n\n\t\t\t\t{item} has been added to your shopping list.\n\n")
        else:
            print("\n\n\t\t\t\tItem is already on the list!\n\n")

    
def view_items():
    # Show the user the list
    print("\n\n\t\t\t\tYour shopping list:")
    for item in shopping_list.readlines():
        print("\t\t\t\t" + item)
    print("\n\n")


def remove_items():
    # Prompt the user for the item to be removed
    item = input("Enter the item you want to remove: ").lower().capitalize()
    if item in shopping_list.readlines():
        with open('shopping_list.txt', 'w') as file:  
            for product in shopping_list.readlines():
                if item != product:
                    file.writelines(product)
                else:
                    print(f"\n\n\t\t\t\t{item} has been removed from your shopping list.\n\n")
    else:
        print(f"\n\n\t\t\t\t{item} is not in your shopping list.\n\n")

# Call the main to start the program
main()
