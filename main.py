import csv


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter category: ")

    with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])

    print("\nExpense added successfully!")


def view_expenses():
    print("\nExpense Summary")
    print("----------------")

    total = 0

    with open("expenses.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])
            total += amount

            print(f"{row['category']}: RM {amount:.2f}")

    print("----------------")
    print(f"Total spent: RM {total:.2f}")


while True:
    print("\nExpense Tracker")
    print("---------------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")