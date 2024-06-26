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

    # print empty string; by default it prints carriage return
    print("")


# function for removing item from the list
def remove_todo(file_name):
    # print("Remove todo")
    todo_name = input("Enter the list item that you want to remove: ")

    # create a new list
    todo_lists = []

    # put all the items into the list except the one user wants to remove
    with open(file_name) as f:
        reader = csv.reader(f)
        # signal for item existence
        is_exist = False
        for row in reader:
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                is_exist = True
    if not is_exist:
        print("No item with that name exists.")

    # write the entire list.csv file with this new list
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        # use writerows function to write the entire list of rows to the file
        writer.writerows(todo_lists)

    # print empty string; by default it prints carriage return
    print("")


# function for marking an item
def mark_todo(file_name):
    # prompt user to input item to be marked DONE
    todo_name = input("Enter the item that you want to mark as DONE: ")

    # create an empty list for items
    todo_lists = []

    # counter for number of items
    i = 0

    # signal for item existence
    is_exist = False

    # prepare the updated list
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        # loop thru the rows
        for row in reader:
            # count each item
            i += 1
            if (todo_name != row[0]):
                todo_lists.append(row)
            else:
                todo_lists.append([row[0], "DONE"])
                # item existing, update signal
                is_exist = True
    
    # check if list has items, header doesn't count
    if i > 1:
        # list is not empty
        # check if item existed
        if is_exist == True:
            # write the updated list to the list file
            with open(file_name, "w") as f:
                writer = csv.writer(f)
                writer.writerows(todo_lists)
        else:
            # item doesn't exist in the list, prompt user
            print("No item with that name exists.")
    else:
        # list is empty, prompt user
        print("No items in the list.")

    # print empty string; by default it prints carriage return
    print("")


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
            print("\nShopping List:")
            
            # loop thru the list counting items and print items if any
            i = 0
            for row in reader:
                i += 1
                if (row[1] == "DONE"):
                    print(f"{row[0]}: DONE")
                else:
                    print(f"{row[0]}: TO BUY")
            
            # empty list
            if i == 0:
                # list is empty, prompt the user
                print("No items in the list.")
            
            # print empty string; by default it prints carriage return
            print("")
    
    except FileNotFoundError:
        print("The list file doesn't exist.")
