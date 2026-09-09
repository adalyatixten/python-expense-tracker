import csv

print("Expense Tracker")
print("---------------")

amount = float(input("Enter expense amount: "))
category = input("Enter category: ")

with open("expenses.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([amount, category])

print()
print("Expense added")
print(f"Amount: RM {amount:.2f}")
print(f"Category: {category}")