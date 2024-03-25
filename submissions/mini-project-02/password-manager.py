import account_manager
import os
import user


def print_menu():
    AccountManager = account_manager.AccountManager()
    while True:
        print("""
            Menu:
                1.) Add account.
                2.) View account.
                3.) Search account.
                4.) Update account.
                5.) Delete account.
                6.) Exit.
        """)
        
        try:
            choice = int(input("Enter your choice: "))
            
            match(choice):
                case 1:
                    os.system('cls')
                    print("====== Add an account ======")
                    AccountManager.add_account()
                case 2:
                    print("""
                        Menu:
                            1.) View one account.
                            2.) View all accounts.
                            3.) Exit.
                    """)
                    
                    try:
                        choice = int(input("Enter your choice: "))
                        print("Invalid input. Please use a number!")
                    
                        match(choice):
                            case 1:
                                os.system('cls')
                                print("====== View an account ======")
                                AccountManager.view_account()
                            case 2:
                                os.system('cls')
                                print("====== View all accounts ======")
                                AccountManager.view_all_accounts()
                            case 3:
                                os.system('cls')
                                continue
                            case default:
                                print("Invalid input. Please try again!")
                    except ValueError:
                        print("Input a valid integer!")
                case 3:
                    os.system('cls')
                    print("====== Search an account ======")
                    AccountManager.search_account()
                case 4:
                    os.system('cls')
                    print("====== Update an account ======")
                    AccountManager.update_account()
                case 5:
                    os.system('cls')
                    print("====== Delete an account ======")
                    AccountManager.delete_account()
                case 6:
                    os.system('cls')
                    break
                case default:
                    print("Invalid input. Please try again!")
        except ValueError:
            print("Input a valid integer!")
            
        
        
    
    
def main():
    running = True

    while running:
        print("====== PASSWORD MANAGER ======")
        print_menu()
        running = False

if __name__ == "__main__":
    main()