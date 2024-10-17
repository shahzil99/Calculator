def meny():
    print("Welcome to my calculator!!")
    print("1. Addition (plus)")
    print("2. Subtraction (minus)")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


while True:
    meny()
    try:
        operator = int(input("Enter your operator (1-5): "))
    except ValueError:
        print("Please enter a number between 1 and 5!")
        continue

    if operator < 1 or operator > 5:
        print(" Invalid operator!")
        continue

    if operator == 5:
        print("Exiting the program! Bye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter numeric values!")
        continue

    if operator == 1:
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operator == 2:
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operator == 3:
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operator == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero! ")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
