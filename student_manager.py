# Student Record Manager (File Handling)

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(f"{name},{marks}\n")

    print("✅ Student added successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("⚠ No records found.\n")
                return

            print("\n📋 Student Records:")
            for line in data:
                name, marks = line.strip().split(",")
                print(f"Name: {name}, Marks: {marks}")
            print()

    except FileNotFoundError:
        print("⚠ File not found. No data yet.\n")


def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice\n")


if __name__ == "__main__":
    main()
