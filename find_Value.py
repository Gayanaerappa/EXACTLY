marks = {
    "Maths": 78,
    "Science": 85,
    "English": 90
}

highest = max(marks, key=marks.get)
print("Highest Marks Subject:", highest)