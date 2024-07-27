# Task 1

def calculate_tax(income, tax_rate):
    tax_amount = income * (tax_rate / 100)
    return tax_amount

user_income = 12345.0
tax_rate = 20.0

tax_to_pay = calculate_tax(user_income, tax_rate)
print(f"The amount of tax to be paid: {tax_to_pay:.2f}")


# Task 2

import random
import string

def generate_password(length, include_special_chars=False):
    characters = string.ascii_letters + string.digits + (string.punctuation if include_special_chars else '')
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password(12))
print(generate_password(16, True))


# Task 3


