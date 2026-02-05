students = {
    "Ram": 85,
    "Sita": 92,
    "Gayana": 88
}

topper = max(students, key=students.get)
print("Topper:", topper)
print("Marks:", students[topper])