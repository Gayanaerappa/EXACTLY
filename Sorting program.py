students = [
    {"id": 3, "name": "Ravi", "age": 21},
    {"id": 1, "name": "Anu", "age": 20},
    {"id": 2, "name": "Sita", "age": 22}
]

print("1. Sort by ID")
print("2. Sort by Name")
print("3. Sort by Age")

choice = input("Enter choice: ")

if choice == "1":
    students.sort(key=lambda x: x["id"])
elif choice == "2":
    students.sort(key=lambda x: x["name"])
elif choice == "3":
    students.sort(key=lambda x: x["age"])

for s in students:
    print(s)