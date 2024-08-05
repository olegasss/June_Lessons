with open('hw_10_test.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f]


print("Read data from the file:")
for line in data:
    print(f"'{line}'")
print()

expense_categories = {}
family_expenses = {}
family_purchases_count = {}

for line in data:
    parts = line.split(', ')
    if len(parts) == 3:
        name, amount, category = parts
        try:
            amount = float(amount)
        except ValueError:
            print(f"Skipping line (invalid amount): {line}")
            continue

        # Update expense categories
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount

        # Update family expenses
        if name in family_expenses:
            family_expenses[name] += amount
            family_purchases_count[name] += 1
        else:
            family_expenses[name] = amount
            family_purchases_count[name] = 1
    else:
        print(f"Skipping line (incorrect format): {line}")

# Print total expenses per category
print("Total expenses for each expense category:")
for category, total in expense_categories.items():
    print(f"{category}: {total:.2f} rubles")
print()

# Print total expenses per family member
print("How much money each family member spent:")
for name, total in family_expenses.items():
    print(f"{name}: {total:.2f} rubles")
print()

# Get user input and print expenses for the specified family member
user_input = input("Enter the name of a family member: ").strip()
if user_input in family_expenses:
    print(
        f"[{user_input}] made {family_purchases_count[user_input]} purchases for a total of {family_expenses[user_input]:.2f} rubles.")
else:
    print(f"No expenses found for [{user_input}].")
