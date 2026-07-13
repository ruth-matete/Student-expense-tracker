import json
import os

FILE_NAME = "expenses.json"


# Load expenses from JSON file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount (Ksh): "))
    except ValueError:
        print("Invalid amount!")
        return

    expense = {
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n===== All Expenses =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} | "
            f"{expense['description']} | "
            f"Ksh {expense['amount']}"
        )


# View total amount spent
def view_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spent: Ksh {total}")


# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses to delete.")
        return

    print("\n===== Delete Expense =====")

    view_expenses(expenses)

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)

            save_expenses(expenses)

            print(
                f"\nDeleted: {removed['category']} - Ksh {removed['amount']}"
            )

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Edit an expense
def edit_expense(expenses):
    if not expenses:
        print("\nNo expenses available to edit.")
        return

    print("\n===== Edit Expense =====")

    view_expenses(expenses)

    try:
        choice = int(input("\nEnter expense number to edit: "))

        if 1 <= choice <= len(expenses):

            print("\nEnter new details:")

            category = input("Enter new category: ")
            description = input("Enter new description: ")

            try:
                amount = float(input("Enter new amount (Ksh): "))
            except ValueError:
                print("Invalid amount!")
                return

            expenses[choice - 1]["category"] = category
            expenses[choice - 1]["description"] = description
            expenses[choice - 1]["amount"] = amount

            save_expenses(expenses)

            print("\nExpense updated successfully!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def menu():
    expenses = load_expenses()

    while True:
        print("\n========== Student Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Delete Expense")
        print("5. Edit Expense")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            view_total(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            edit_expense(expenses)

        elif choice == "6":
            print("\nThank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
menu()