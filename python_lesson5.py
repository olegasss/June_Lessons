# Task1

for number in range(1, 101):
    if number % 7 == 0:
        print(number)

# Task2

summa = 0
count = 1

for count in range(1, 100):
    if count % 2 != 0:
        summa += count

print(f"The sum of odd integers from 1 to 99 is: {summa}")

# Task3

number = 1
line_count = 0

while number <= 200:
    print(number, end=' ')
    number += 1
    line_count += 1

    if line_count == 5:
        print()
        line_count = 0

# Task4

n = int(input("Enter a number n: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial number {n} is {factorial}")


# Task5


def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i * n}")


if __name__ == "__main__":
    multiplication_table(5)


# Task6

def draw_rectangle(height, width):
    for i in range(height):
        print('*' * width)


height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Task7

numbers = [0, 5, 2, 4, 7, 1, 3, 19]

count_odd = 0

for num in numbers:
    if num % 2 != 0:
        count_odd += 1

print("number of unfairnumbers in the list:", count_odd)

# Task8

import random

first_list = [random.randint(1, 10) for _ in range(4)]
second_list = first_list + [2 * num for num in first_list]

print("Was →", first_list)
print("Became →", second_list)


#Task9

import random

salaries = [random.randint(1000, 5000) for _ in range(12)]

average_salary = sum(salaries) / len(salaries)

print("Salary per month:", salaries)
print("Average salary:", average_salary)


#Task10

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Matrix:")
for row in matrix:
    print(row)

sum_elements = sum(sum(row) for row in matrix)

print("\nSum of matrix elements:", sum_elements)


#Task11
def reverse_list(input_list):
    return input_list[::-1]

original_list = [7, 2, 9, 4]
reversed_list = reverse_list(original_list)

print("Original list:", original_list)
print("Reversed list:", reversed_list)


#Task12

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num)