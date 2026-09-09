import csv

print("Expense Tracker")
print("---------------")

amount = float(input("Enter expense amount: "))
category = input("Enter category: ")

# Save the new expense
with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([amount, category])

print()
print("Expense added")
print(f"Amount: RM {amount:.2f}")
print(f"Category: {category}")

# Show all expenses and calculate total
print("\nExpense Summary")
print("---------------")

total = 0

with open("expenses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        expense_amount = float(row["amount"])
        total += expense_amount

        print(f"{row['category']}: RM {expense_amount:.2f}")

print("---------------")
print(f"Total spent: RM {total:.2f}")