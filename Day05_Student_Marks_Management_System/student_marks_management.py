print("=" * 55)
print("      STUDENT MARKS MANAGEMENT SYSTEM")
print("=" * 55)

students = {}


def add_student():
    name = input("\nEnter Student Name: ").title()

    if name in students:
        print("Student already exists!")
        return

    try:
        marks = float(input("Enter Marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students[name] = marks
        print(f"{name} added successfully!")

    except ValueError:
        print("Please enter valid marks.")


def view_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\nStudent Records")
    print("-" * 35)

    print("{:<20} {:>10}".format("Student", "Marks"))
    print("-" * 35)

    for name, marks in students.items():
        print("{:<20} {:>10}".format(name, marks))


def search_student():
    name = input("\nEnter Student Name: ").title()

    if name in students:
        print(f"{name} scored {students[name]} marks.")
    else:
        print("Student not found.")


def update_marks():
    name = input("\nEnter Student Name: ").title()

    if name not in students:
        print("Student not found.")
        return

    try:
        marks = float(input("Enter New Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        students[name] = marks
        print("Marks updated successfully!")

    except ValueError:
        print("Invalid marks.")


def delete_student():
    name = input("\nEnter Student Name: ").title()

    if name in students:
        del students[name]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_topper():

    if not students:
        print("No student records found.")
        return

    topper = max(students, key=students.get)

    print("\nTopper")
    print("-" * 30)
    print(f"Name : {topper}")
    print(f"Marks: {students[topper]}")


while True:

    print("\n" + "=" * 55)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Exit")
    print("=" * 55)

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_topper()

    elif choice == "7":
        print("\nThank you for using the Student Marks Management System!")
        break

    else:
        print("Invalid choice. Please try again.")