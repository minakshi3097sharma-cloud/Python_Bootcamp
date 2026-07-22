FILE_NAME = "notes.txt"

def save_note():
    note = input("\nEnter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("✅ Note saved successfully!")


def read_notes():

    try:
        with open(FILE_NAME, "r") as file:

            notes = file.readlines()

            if not notes:
                print("\nNo notes available.")
                return

            print("\nYour Notes")
            print("-" * 40)

            for index, note in enumerate(notes, start=1):
                print(f"{index}. {note.strip()}")

    except FileNotFoundError:
        print("\nNo notes found.")


def delete_notes():

    with open(FILE_NAME, "w") as file:
        pass

    print("✅ All notes deleted successfully!")


while True:

    print("\n" + "=" * 45)
    print("         SIMPLE NOTES APP")
    print("=" * 45)

    print("1. Save Note")
    print("2. Read Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        save_note()

    elif choice == "2":
        read_notes()

    elif choice == "3":
        delete_notes()

    elif choice == "4":
        print("\nThank you for using Notes App.")
        break

    else:
        print("Invalid choice.")