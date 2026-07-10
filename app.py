import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    print("\n--- Add Expense ---")

    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses = load_expenses()

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("\n✅ Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    print("\n--- Your Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - Ksh {expense['amount']}")


def view_total():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    print("\n--- Total Spending ---")
    print(f"Total Spent: Ksh {total}")


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

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_total()

    elif choice == "5":
        print("\nThank you for using Student Expense Tracker!")
        break

    else:
        print("\nThis option is coming soon...")