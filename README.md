# FEB24 T1A3 Terminal App

## URL of the GitHub Repo
https://github.com/amer-riaz/FEB24-t1a3.git

## Description
This terminal application written in Python3 is a basic terminal application. It lets the user create a shopping list with one or more items. The app stores the shopping list in a CSV file on the file system. Each item is by default marked 'to buy'. As the user has bought some item, they can use the application to mark the item 'done', one at a time. The user can add new items to the list, one at a time. Similarly, the user can change or remove items, one at a time. After using the application user can quit the application using.

## Coding Style Guide
PEP8 Style Guide followed
URL: https://peps.python.org/pep-0008/

## List of Features
The following menu options are presented by the app and user can input their selection number:
1. Enter 1 to ADD item to the list.
2. Enter 2 to REMOVE item from the list.
3. Enter 3 to MARK any item as complete.
4. Enter 4 to VIEW todo list items.
5. Enter 5 to EXIT.
Enter your selection:

### 1. Enter 1 to ADD item to the list.
If user inputs 1, they are requested to input the item name like:
Enter name of the item to add: 
User then inputs the name. The app then adds the item to the list. The item is added to the list marked as TO BUY, by defualt.

### 2. Enter 2 to REMOVE item from the list.
If user inputs 2, they are requested to input the item name like:
Enter name of the item to remove: 
User then inputs the name. The app then removes the item from the list.

### 3. Enter 3 to MARK any item as complete.
If user inputs 3, they are requested to input the item name like:
Enter name of the item to mark: 
User then inputs the name. The app then marks the item DONE.

### 4. Enter 4 to VIEW todo list items.
If user inputs 4, the app prints the items in the list, for example:
Apples, TO BUY
Oranges, DONE
bread, TO BUY

### 5. Enter 5 to EXIT.
If user inputs 5, the app terminates.