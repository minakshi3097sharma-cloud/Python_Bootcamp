print("=" * 45)
print("         GRADE CALCULATOR")
print("=" * 45)

# Input
marks = float(input("Enter your Marks (0-100): "))

# Validation
if marks < 0 or marks > 100:
    print("\nInvalid Marks! Please enter marks between 0 and 100.")

# Grade Calculation
elif marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Output
if 0 <= marks <= 100:
    print("\n" + "=" * 45)
    print("             RESULT")
    print("=" * 45)
    print(f"Marks : {marks}")
    print(f"Grade : {grade}")
    print("=" * 45)
    print("Thank You!")