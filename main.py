# main.py
# implementation of the main logic of the app


# print a welcome message
print("Welcome to the Shopping list app.")


# function to present app menu
def create_menu():
    print("1. Enter 1 to ADD item to the list.")
    print("2. Enter 2 to REMOVE item from the list.")
    print("3. Enter 3 to MARK an item as done.")
    print("4. Enter 4 to VIEW list items.")
    print("5. Enter 5 to EXIT.")

    user_choice = input("Enter your selection: ")
    return user_choice


# variable to record user's selection
choice = ""

while choice != "5":
    choice = create_menu()

    if (choice == "1"):
        print("Item added.")
        # add_todo(file_name)
    elif (choice == "2"):
        print("Item removed.")
        # remove_todo(file_name)
    elif (choice == "3"):
        print("Item marked.")
        # mark_todo(file_name)
    elif (choice == "4"):
        print("List printed.")
        # view_todo(file_name)
    elif (choice == "5"):
        print("You entered 5 to exit.")
    else:
        print("Please only enter the options shown above.")


print("Thank you for using my Shopping list app.")