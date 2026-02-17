import os
from datetime import datetime

FILENAME = "journal.txt"

# 1. Add New Entry
def add_entry():
    entry = input("Enter your journal entry:\n")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILENAME, "a") as file:
        file.write(f"[{time}]\n")
        file.write(entry + "\n\n")
    
    print("Entry added successfully!\n")


# 2. View All Entries
def view_entries():
    if not os.path.exists(FILENAME):
        print("No journal entries found. Start by adding a new entry!\n")
        return

    with open(FILENAME, "r") as file:
        print("\nYour Journal Entries:")
        print("--------------------------")
        print(file.read())


# 3. Search Entry
def search_entry():
    if not os.path.exists(FILENAME):
        print("Error: The journal file does not exist.")
        print("Please add a new entry first.\n")
        return

    keyword = input("Enter a keyword or date to search: ")
    found = False

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    print("\nMatching Entries:")
    print("--------------------------")

    for line in lines:
        if keyword.lower() in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No entries were found for the keyword:", keyword)
    print()


# 4. Delete All Entries
def delete_entries():
    if not os.path.exists(FILENAME):
        print("No journal entries to delete.\n")
        return

    choice = input("Are you sure you want to delete all entries? (yes/no): ")
    
    if choice.lower() == "yes":
        os.remove(FILENAME)
        print("All journal entries have been deleted.\n")
    else:
        print("Delete cancelled.\n")


# Main Menu
while True:
    print("Welcome to Personal Journal Manager!")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    option = input("Select an option (1-5): ")

    if option == "1":
        add_entry()
    elif option == "2":
        view_entries()
    elif option == "3":
        search_entry()
    elif option == "4":
        delete_entries()
    elif option == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.\n")
