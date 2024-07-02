#Task 1

number = float(input("Type number: "))
if number < 0:
    print(f"input number: {number}")
else:
    print("Enter a valid number")


#Task 2

def check_integer_less_than_20():
    try:
        user_input = int(input("Type your number: "))
        if user_input < 20:
            print("input number less 20.")
        else:
            print("input number not less 20.")
    except ValueError:
        print("enter a valid integer number.")
check_integer_less_than_20()


#Task 3

user_input = int(input("Enter your integer: "))
try:
    number = int(user_input)
except ValueError:
    print("Entered a valid integer.")
    exit()

if number == 0:
    print("Entered value is zero.")
else:
    print("Entered value is not zero.")



#Task 4

user_input = input("Type your integer: ")
try:
    number = int(user_input)
    if number % 2 == 0:
        print(f"the number {number} is odd.")
    else:
        print(f"the number {number} is even.")
except ValueError:
    print("ValueError: enter the number a valid.")



#Task 5

num1 = float(input("Type first number: "))
num2 = float(input("Type second number: "))
num3 = float(input("Type third number: "))

max_num = max(num1, num2, num3)

print(f"Largest number: {max_num}")
