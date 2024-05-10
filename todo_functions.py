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
        writer.writerow([todo_name, "DONE"])


# function for removing item from the list
def remove_todo():
    print("Remove todo")


# function for marking an item
def mark_todo():
    print("Mark todo")


# function for viewing the list
def view_todo():
    print("View todo")
