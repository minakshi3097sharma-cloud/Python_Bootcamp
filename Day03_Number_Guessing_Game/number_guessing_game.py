import random

print("=" * 40)
print("       NUMBER GUESSING GAME")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")