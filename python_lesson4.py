#Task 1

def is_lucky_ticket(number):
    if not 1000 <= number <= 9999:
        raise ValueError("The number must be a four-digit integer.")
    number_str = str(number)
    return sum(map(int, number_str[:2])) == sum(map(int, number_str[2:]))

number = 1322
print(f"{number} is {'a lucky ticket' if is_lucky_ticket(number) else 'not a lucky ticket'}.")


#Task 2

def is_palindrome(number):
    if not 100000 <= number <= 999999:
        raise ValueError("The number must be a six-digit integer.")
    return str(number) == str(number)[::-1]

number = int(input("Enter a six-digit number: "))
print(f"{number} is {'a palindrome' if is_palindrome(number) else 'not a palindrome'}.")


#Task 3

def is_point_inside_circle(x, y, radius=4):
    return x**2 + y**2 <= radius**2

x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

if is_point_inside_circle(x, y):
    print(f"The point ({x}, {y}) is inside the circle.")
else:
    print(f"The point ({x}, {y}) is outside the circle.")