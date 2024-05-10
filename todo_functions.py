# todo_functions.py
# implementation of the features of the app


# System packages
import csv


# function for adding item to list
def add_todo(file_name):
    todo_name = input("Enter a list item: ")
    
    # with block for appending the item to the file
    with open(file_name, "a") as f:
        # use a writer object that helps us writing to the csv file
        writer = csv.writer(f)
        writer.writerow([todo_name, "TO BUY"])


# function for removing item from the list
def remove_todo(file_name):
    # print("Remove todo")
    todo_name = input("Enter the list item that you want to remove: ")


# function for marking an item
def mark_todo():
    print("Mark todo")


# function for viewing the list
def view_todo(file_name):
    # try - catch block for checking if the list file exists
    try:
        with open(file_name, "r") as f:
            # file exists
            
            # use reader object from csv package for reading from the csv file
            reader = csv.reader(f)

            # we don't need the header row; so we skip it
            reader.__next__()
            
            # printing list items
            print("\nShopping List:");
            for row in reader:
                if (row[1] == "DONE"):
                    print(f"{row[0]}: DONE")
                else:
                    print(f"{row[0]}: TO BUY")
            print("\n");
    
    except FileNotFoundError:
        print("The list file doesn't exist. Add item(s).")
