#Task 1

def get_apart_info(apart_number):
    apart_per_floor, floors, entrances = 4, 9, 4
    if not (1 <= apart_number <= apart_per_floor * floors * entrances):
        return "No flat number"
    entrance = (apart_number - 1) // (apart_per_floor * floors) + 1
    remaining = (apart_number - 1) % (apart_per_floor * floors)
    return entrance, remaining // apart_per_floor + 1, remaining % apart_per_floor + 1

result = get_apart_info(int(input("Enter flat number: ")))
print(result if isinstance(result, str) else f"Entrance: {result[0]}, Floor: {result[1]}, Apart on floor: {result[2]}")


#Task 2

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 == 0) or (year % 400 == 0):
        return True
    else:
        return False
def days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365
def main():
    year = int(input("Enter a year: "))
    num_days = days_in_year(year)
    print(f"The year {year} has {num_days} days.")
if __name__ == "__main__":
    main()

#Task 3

a, b, c = int(input('a=')), int(input('b=')), int(input('c='))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("The sides can form a triangle.")
else:
    print("The sides cannot form a triangle.")



