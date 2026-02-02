employees = [
    [1, "Ravi", 20000],
    [2, "Anu", 30000],
    [3, "Kiran", 15000],
    [4, "Meena", 40000],
    [5, "John", 25000]
]

# Lambda functions
hra = lambda basic: basic * 0.20
da = lambda basic: basic * 0.10
gross = lambda basic: basic + hra(basic) + da(basic)

print("Employee Salary Details\n")

for emp in employees:
    emp_id = emp[0]
    name = emp[1]
    basic = emp[2]

    print("ID:", emp_id)
    print("Name:", name)
    print("Basic Salary:", basic)
    print("HRA:", hra(basic))
    print("DA:", da(basic))
    print("Gross Salary:", gross(basic))
    print("------------------------")

# Filter employees with gross salary above 30000
high_salary = list(filter(lambda e: gross(e[2]) > 30000, employees))

print("\nEmployees with Gross Salary > 30000")
for e in high_salary:
    print(e[1], "->", gross(e[2]))

# Sort employees by basic salary
employees.sort(key=lambda x: x[2])

print("\nEmployees Sorted by Basic Salary")
for e in employees:
    print(e[1], ":", e[2])
 




