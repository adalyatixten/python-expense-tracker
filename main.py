import csv
from datetime import date


def add_expense():
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    expense_date = date.today().isoformat()

    with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([expense_date, amount, category])

    print("\nExpense added successfully!")
    print(f"Date: {expense_date}")
    print(f"Amount: RM {amount:.2f}")
    print(f"Category: {category}")


def view_expenses():
    print("\nExpense Summary")
    print("--------------------------------")

    total = 0

    with open("expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])
            total += amount

            print(
                f"{row['date']} | "
                f"{row['category']} | "
                f"RM {amount:.2f}"
            )

    print("--------------------------------")
    print(f"Total spent: RM {total:.2f}")


while True:
    print("\nExpense Tracker")
    print("---------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")