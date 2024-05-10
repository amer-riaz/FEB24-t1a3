# main.py
# implementation of the main logic of the app


# System packages
import os.path


# Imports of our own functions from other files
from todo_functions import add_todo, remove_todo, mark_todo, view_todo


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


# csv file is comma separated file
file_name = "list.csv"

# if the csv file doesn't exist, create the file
if (not os.path.isfile(file_name)):
    print("Creating file as it doesn't exist")
    # create the file
    todo_file = open(file_name, "w")
    # enter the headings into the file
    todo_file.write("title,completed\n")
    # close the file
    todo_file.close()

# variable to record user's selection
choice = ""

while choice != "5":
    choice = create_menu()

    if (choice == "1"):
        # print("Item added.")
        add_todo()
    elif (choice == "2"):
        # print("Item removed.")
        remove_todo()
    elif (choice == "3"):
        # print("Item marked.")
        mark_todo()
    elif (choice == "4"):
        # print("List printed.")
        view_todo()
    elif (choice == "5"):
        print("You entered 5 to exit.")
    else:
        print("Please only enter the options shown above.")


# exit the app saying Thank You to user
print("Thank you for using my Shopping list app.")