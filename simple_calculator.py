print("=" * 40)
print("    SIMPLE CALCULATOR USING FUNCTIONS")
print("=" * 40)


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return None

    return first_number / second_number


while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1–5): ")

    if choice == "5":
        print("Calculator closed. Thank you!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select a number from 1 to 5.")
        continue

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        if choice == "1":
            result = add(first_number, second_number)
            operation = "+"

        elif choice == "2":
            result = subtract(first_number, second_number)
            operation = "-"

        elif choice == "3":
            result = multiply(first_number, second_number)
            operation = "×"

        else:
            result = divide(first_number, second_number)
            operation = "÷"

            if result is None:
                print("Error: Division by zero is not allowed.")
                continue

        print("\n" + "=" * 40)
        print("RESULT")
        print("=" * 40)
        print(f"{first_number} {operation} {second_number} = {result}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")