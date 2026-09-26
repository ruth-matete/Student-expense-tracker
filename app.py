
import json
import os
from datetime import datetime

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


# Display expenses
def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['category']} | "
            f"{expense['description']} | "
            f"Ksh {expense['amount']:.2f} | "
            f"Date: {expense.get('date', 'N/A')}"
        )


# Add a new expense
def add_expense(expenses):
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount (Ksh): "))
    except ValueError:
        print("Invalid amount!")
        return

    # Automatically record today's date
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"Expense added successfully! Date recorded: {date}")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\n===== All Expenses =====")
    display_expenses(expenses)


# View total amount spent
def view_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Spent: Ksh {total:.2f}")


# Delete an expense
def delete_expense(expenses):
    if not expenses:
        print("\nNo expenses to delete.")
        return

    print("\n===== Delete Expense =====")
    display_expenses(expenses)

    try:
        choice = int(input("\nEnter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)

            save_expenses(expenses)

            print(
                f"\nDeleted: {removed['category']} - "
                f"Ksh {removed['amount']:.2f}"
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
    display_expenses(expenses)

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

            # Automatically update the date when the expense is edited
            date = datetime.now().strftime("%Y-%m-%d")

            expenses[choice - 1]["category"] = category
            expenses[choice - 1]["description"] = description
            expenses[choice - 1]["amount"] = amount
            expenses[choice - 1]["date"] = date

            save_expenses(expenses)

            print(
                f"\nExpense updated successfully! "
                f"Date updated to: {date}"
            )

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Search expenses
def search_expenses(expenses):
    if not expenses:
        print("\nNo expenses available to search.")
        return

    print("\n===== Search Expenses =====")

    search_term = input("Enter search term: ").lower().strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    results = []

    for expense in expenses:
        category = expense["category"].lower()
        description = expense["description"].lower()

        if search_term in category or search_term in description:
            results.append(expense)

    if results:
        print(f"\n===== Search Results for '{search_term}' =====")
        display_expenses(results)
    else:
        print(f"\nNo expenses found matching '{search_term}'.")


# Filter expenses by category
def filter_by_category(expenses):
    if not expenses:
        print("\nNo expenses available.")
        return

    print("\n===== Filter by Category =====")

    category = input("Enter category: ").lower().strip()

    if not category:
        print("Category cannot be empty.")
        return

    results = []

    for expense in expenses:
        if expense["category"].lower() == category:
            results.append(expense)

    if results:
        print(f"\n===== Expenses in '{category.title()}' =====")
        display_expenses(results)
    else:
        print(f"\nNo expenses found in the category '{category}'.")


# Filter expenses by date
def filter_by_date(expenses):
    if not expenses:
        print("\nNo expenses available.")
        return

    print("\n===== Filter by Date =====")

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Please use YYYY-MM-DD.")
        return

    results = []

    for expense in expenses:
        if expense.get("date") == date:
            results.append(expense)

    if results:
        print(f"\n===== Expenses on {date} =====")
        display_expenses(results)
    else:
        print(f"\nNo expenses found for {date}.")


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
        print("6. Search Expenses")
        print("7. Filter by Category")
        print("8. Filter by Date")
        print("9. Exit")

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
            search_expenses(expenses)

        elif choice == "7":
            filter_by_category(expenses)

        elif choice == "8":
            filter_by_date(expenses)

        elif choice == "9":
            print("\nThank you for using Student Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
menu()