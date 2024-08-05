# Expenses data
data = [
[1, "Bob Simson", 19.58, "decorations"],
[2, "Mary", 66.7, "food"],
[3, "Mary", 98.91, "toys"],
[4, "Aleksa", 72.29, "drinks"],
[5, "Maria Simson", 84.48, "food"],
[6, "Aleksa", 100.41, "accessories"],
[7, "Mary", 19.9, "accessories"],
[8, "Bob Simson", 83.88, "drinks"],
[9, "Bob Simson", 58.21, "instruments"],
[10, "Maria Simson", 20.61, "accessories"],
[11, "Aleksa", 37.74, "drinks"],
[12, "Mary", 12.32, "drinks"],
[13, "Maria Simson", 32.11, "toys"],
[14, "Maria Simson", 94.73, "instruments"],
[15, "Mary", 52.48, "clothes"],
[16, "Maria Simson", 87.64, "drinks"],
[17, "Jack", 70.86, "clothes"],
[18, "Bob Simson", 134.5, "drinks"],
[19, "Jack", 4.23, "instruments"],
[20, "Jack", 62.59, "food"],
[21, "Mary", 110.69, "accessories"],
[22, "Bob Simson", 119.0, "drinks"],
[23, "Maria Simson", 38.17, "instruments"],
[24, "Maria Simson", 31.82, "food"],
[25, "Aleksa", 146.64, "food"],
# ... (the rest of the data)
]

# 1. Total expenses for each category
expense_categories = {}
for _, _, amount, category in data:
    print(f"Amount: {amount}, Category: {category}")
    if category not in expense_categories:
        expense_categories[category] = 0
    expense_categories[category] += amount
print("Total expenses for each category:")
for category, total in expense_categories.items():
    print(f"{category.capitalize()}: {total:.2f}$")

# 2. Total expenses for each family member
family_expenses = {}
for _, name, amount, category in data:
    print(f"Name: {name}, Amount: {amount}, Category: {category}")
    if name not in family_expenses:
        family_expenses[name] = 0
    family_expenses[name] += amount
print("\nTotal expenses for each family member:")
for name, total in family_expenses.items():
    print(f"{name}: {total:.2f}$")
#
# # 3. Expenses of a specific family member
user_name = input("Enter the name of the family member: ")
user_expenses = [exp for _, name, exp, _ in data if name == user_name]
if user_expenses:
    total_user_expenses = sum(user_expenses)
    print(f"[{user_name}] spent {total_user_expenses:.2f}$ in total")
else:
    print(f"\nNo expenses found for {user_name}.")