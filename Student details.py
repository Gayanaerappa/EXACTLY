students = []   # list to store all students

for i in range(2):
    print(f"\nEnter details of Student {i+1}")

    student = {}

    student["name"] = input("Enter student name: ")
    student["maths"] = int(input("Enter Maths marks: "))
    student["science"] = int(input("Enter Science marks: "))
    student["english"] = int(input("Enter English marks: "))

    total = student["maths"] + student["science"] + student["english"]
    average = total / 3

    student["total"] = total
    student["average"] = average

    students.append(student)
 
# Display all students
print("\nAll Student Details")
for s in students:
    print(s)
print(students)  
print(student)