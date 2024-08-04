# Общие расходы по категориям
expenses_by_category = get_expenses_by_category(df)
print("Общие расходы по категориям:")
for category, amount in expenses_by_category\.items():
    print(f"{category}: {amount:\.2f}")

# Расходы каждого члена семьи
expenses_by_person = get_expenses_by_person(df)
print("\nРасходы каждого члена семьи:")
for person, amount in expenses_by_person\.items():
    print(f"{person}: {amount:\.2f}")

# Ввод имени члена семьи
person_name = input("Введите имя члена семьи (на кириллице): ")
num_purchases, total_amount = get_person_purchases(df, person_name)
print(f"Количество покупок {person_name}: {num_purchases}")
print(f"Общая сумма покупок {person_name}: {total_amount:\.2f}")
