import math

while True:
    value = input("Enter a number (or 'q' to quit): ")

    if value.lower() == 'q':
        break

    try:
        num = float(value)

        if num < 0:
            print("Square root of negative numbers is not allowed.")
        else:
            print("Square root =", math.sqrt(num))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
