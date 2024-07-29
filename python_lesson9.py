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

from typing import List
import string


def text_to_numbers(text: str) -> List[int]:
    for char in string.punctuation:
        text = text.replace(char, ' ')
    return list(map(int, text.split()))


def is_arithmetic_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    d = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != d:
            return False
    return True


def is_geometric_progression(numbers: List[int]) -> bool:
    if len(numbers) < 2:
        return False

    q = numbers[1] // numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] // numbers[i - 1] != q:
            return False
    return True


def next_arihmetic_number(numbers: List[int]) -> int:
    d = numbers[1] - numbers[0]
    return numbers[-1] + d


def next_geometric_number(numbers: List[int]) -> int:
    q = numbers[1] // numbers[0]
    return numbers[-1] * q


def base(numbers: List[int]) -> int:
    if is_arithmetic_progression(numbers):
        return next_arihmetic_number(numbers)

    if is_geometric_progression(numbers):
        return next_geometric_number(numbers)

    return None


def main():
    text = input("Enter a list of numbers separated by a space: ")
    numbers = text_to_numbers(text)
    res = base(numbers)
    if res:
        print(f"The next number in the sequence is: {res}")
    else:
        print(f"The sequence is not defined by an arithmetic or geometric progression.")


if __name__ == "__main__":
    main()


# Task 5

import inflect
def convert_to_words(amount):
    p = inflect.engine()
    dollars, cents = map(int, amount.split('.'))
    return (f"{p.number_to_words(dollars)} dollar{'s' if dollars != 1 else ''} /n"
            f"{p.number_to_words(cents)} cent{'s' if cents != 1 else ''}")

amount = "561.98"
print(convert_to_words(amount))
