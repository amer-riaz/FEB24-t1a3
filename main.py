# main.py
# implementation of the main logic of the app


# System packages
import os.path


# Imports of our own functions from other files
from todo_functions import add_todo, remove_todo, mark_todo, view_todo


# print a welcome message
print("\nWelcome to the Shopping list app.")


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

# main loop to keep asking for selection until 5 is input to exit
while choice != "5":
    # print the menu and save user's selection
    choice = create_menu()

    # perform according to user's selection
    if (choice == "1"):
        # add item given by user
        add_todo(file_name)
    elif (choice == "2"):
        # remove item specified by user
        remove_todo(file_name)
    elif (choice == "3"):
        # mark item specified by user
        # print("Item marked.")
        mark_todo(file_name)
    elif (choice == "4"):
        # print the list
        view_todo(file_name)
    elif (choice == "5"):
        # print("You entered 5 to exit.")
        # print empty string; by default it prints carriage return
        print("")
    else:
        print("Please only enter the options shown above.")


# exit the app saying Thank You to user
print("Thank you for using my Shopping list app.\n")