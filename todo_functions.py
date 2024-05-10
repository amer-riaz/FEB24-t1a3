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

    # create a new list
    todo_lists = []

    # put all the items into the list except the one they want to delete
    with open(file_name) as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.\n")

    # write the entire list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        # use writerows function to write the entire list of rows to the file
        writer.writerows(todo_lists)


# function for marking an item
def mark_todo(file_name):
    # prompt user to input item to be marked DONE
    todo_name = input("Enter the item that you want to mark as DONE: ")

    # create an empty list for items
    todo_lists = []

    # prepare the updated list
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "DONE"])

    # write the updated list to the list file
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_lists)
    


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
            # loop thru the list
            for row in reader:
                if (row[1] == "DONE"):
                    print(f"{row[0]}: DONE")
                else:
                    print(f"{row[0]}: TO BUY")
            # print empty string; by default it prints carriage return
            print("");
    
    except FileNotFoundError:
        print("The list file doesn't exist. Add item(s).")
