def read_data(filename):
    """Function read_data(filename): Uses split(' ') to split a string by spaces."""
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(' ')
            if len(parts) >= 4:
                # Reconstruct name
                name_parts = parts[1:-2]
                name = ' '.join(name_parts)
                amount_str = parts[-2]
                amount = float(amount_str.replace('$', ''))
                category = parts[-1]
                data.append((name, amount, category))
            else:
                print(f"Skipping line: {line.strip()}")
    return data


def calculate_expenses_by_category(data):
    """Calculates the total expenses by category."""
    expense_categories = {}
    for _, amount, category in data:
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    return expense_categories


def calculate_expenses_by_family_member(data):
    """Calculates the total expenses by each family member."""
    family_expenses = {}
    for name, amount, _ in data:
        if name in family_expenses:
            family_expenses[name] += amount
        else:
            family_expenses[name] = amount
    return family_expenses


def calculate_user_expenses(data, user_name):
    """Calculates the number of purchases and total expenses for the given family member."""
    user_expenses = 0.0
    purchase_count = 0
    for name, amount, _ in data:
        if name == user_name:
            user_expenses += amount
            purchase_count += 1
    return purchase_count, user_expenses


def print_expenses_by_category(expense_categories):
    """Prints the total expenses by category."""
    print("Total expenses by category:")
    for category, total in expense_categories.items():
        print(f"{category}: {total:.2f} USD")
    print()


def print_expenses_by_family_member(family_expenses):
    """Prints the total expenses by each family member."""
    print("Total expenses by family member:")
    for name, total in family_expenses.items():
        print(f"{name}: {total:.2f} USD")
    print()


def main(filename):
    data = read_data(filename)

    expense_categories = calculate_expenses_by_category(data)
    family_expenses = calculate_expenses_by_family_member(data)

    print_expenses_by_category(expense_categories)
    print_expenses_by_family_member(family_expenses)

    user_input = input("Enter the name of a family member: ").strip()
    purchase_count, user_expenses = calculate_user_expenses(data, user_input)
    if purchase_count > 0:
        print(f"[{user_input}] made {purchase_count} purchases totaling {user_expenses:.2f} USD.")
    else:
        print(f"No expenses found for [{user_input}].")


if __name__ == "__main__":
    filename = 'hw_10_test.txt'
    main(filename)
