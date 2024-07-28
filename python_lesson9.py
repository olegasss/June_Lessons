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

num1 = 999
num2 = 999
palindrome_list = []

while num1 >= 100:
    while num2 >= 100:
        word = num1 * num2
        word_str = str(word)
        if word > 100000 and word_str == word_str[::-1]:
            palindrome_list.append(word)
        num2 -= 1
    num1 -= 1
    num2 = 999

palindrome_list.sort(reverse=True)
print(palindrome_list[0])


# Task 4










# Task 5

import inflect
def convert_to_words(amount):
    p = inflect.engine()
    dollars, cents = map(int, amount.split('.'))
    return (f"{p.number_to_words(dollars)} dollar{'s' if dollars != 1 else ''} /n"
            f"{p.number_to_words(cents)} cent{'s' if cents != 1 else ''}")

amount = "561.98"
print(convert_to_words(amount))
