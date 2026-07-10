import json
import os


def menu():
    print("\n" + "=" * 35)
    print("     STUDENT EXPENSE TRACKER")
    print("=" * 35)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Delete Expense")
    print("5. Exit")


while True:
    menu()

    choice = input("\nChoose an option (1-5): ")

    if choice == "5":
        print("\nThank you for using Student Expense Tracker!")
        break

    else:
        print("\nThis option is coming soon...")