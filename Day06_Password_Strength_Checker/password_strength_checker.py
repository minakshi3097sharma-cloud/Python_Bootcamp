import string

print("=" * 50)
print("        PASSWORD STRENGTH CHECKER")
print("=" * 50)


def check_password(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    print("\nPassword Analysis")
    print("-" * 30)

    print(f"Length           : {len(password)}")
    print(f"Uppercase Letter : {'Yes' if any(c.isupper() for c in password) else 'No'}")
    print(f"Lowercase Letter : {'Yes' if any(c.islower() for c in password) else 'No'}")
    print(f"Number           : {'Yes' if any(c.isdigit() for c in password) else 'No'}")
    print(f"Special Symbol   : {'Yes' if any(c in string.punctuation for c in password) else 'No'}")

    print("\nPassword Strength")

    if score == 5:
        print("🟢 Strong Password")

    elif score >= 3:
        print("🟡 Medium Password")

    else:
        print("🔴 Weak Password")


password = input("\nEnter your password: ")

check_password(password)