# Adventure Game

# Main function
def main():
    print("""
    ███████╗██╗███╗   ██╗██████╗     ████████╗██╗  ██╗███████╗     ██████╗ █████╗ ████████╗
    ██╔════╝██║████╗  ██║██╔══██╗    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██╔══██╗╚══██╔══╝
    █████╗  ██║██╔██╗ ██║██║  ██║       ██║   ███████║█████╗      ██║     ███████║   ██║   
    ██╔══╝  ██║██║╚██╗██║██║  ██║       ██║   ██╔══██║██╔══╝      ██║     ██╔══██║   ██║   
    ██║     ██║██║ ╚████║██████╔╝       ██║   ██║  ██║███████╗    ╚██████╗██║  ██║   ██║   
    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝   ╚═╝""")
    while True:
        print("Menu:\n\t1. Start\n\t2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            start_game()
            break
        elif choice == '2':
            exit_game()
            break
        else:
            print("Choice is not on the menu! Please try again...")

# When user choose to start
def start_game():
    # Prompt the user to choose a location
    count = 0
    while True:
        print("Which location do you want to check?")
        print("\t1. Above the tree\n\t2. Under your bed\n\t3. Inside the box\n\t4. Mystery house")
        choice = input("Enter your choice: ")
        if choice == '1':
            above_the_tree()
            break
        elif choice == '2':
            under_your_bed()
            break
        elif choice == '3':
            inside_the_box()
            break
        elif choice == '4':
            mystery_house()
            break
        else:
            print("Choice is not on the menu! Please try again...")
    
# When user choose to exit       
def exit_game():
    print("Aww, you don't like cats? :(")


def above_the_tree():
    print("There's a cat stuck on the tree. Help it?")
    while True:
        choice = input("Enter your choice (Y/N): ")
        if choice == 'Y':
            print("Purr! You found the cat!!")
            break
        elif choice == 'N':
            exit_game()
            break
        else:
            print("That's not an option. Please try again...")

def under_your_bed():
    print("There's something glowing under your bed. Check it?")
    while True:
        choice = input("Enter your choice (Y/N): ")
        if choice == 'Y':
            print("Purr! You found the cat!!")
            break
        elif choice == 'N':
            exit_game()
            break
        else:
            print("That's not an option. Please try again...")


def inside_the_box():
    print("Something's rustling inside the box. Look inside?")
    while True:
        choice = input("Enter your choice (Y/N): ")
        if choice == 'Y':
            print("Purr! You found the cat!!")
            break
        elif choice == 'N':
            exit_game()
            break
        else:
            print("That's not an option. Please try again...")


def mystery_house():
    print("pur.")
    print("purr..")
    print("purrr...")
    print("Cats are everywhere!")


# Calling the main
main()
