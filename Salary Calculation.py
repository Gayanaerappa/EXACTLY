basic = float(input("Enter Basic Salary: "))

# HRA = 20% of Basic
hra = basic * 0.20

# DA = 10% of Basic
da = basic * 0.10

# Gross Salary
gross_salary = basic + hra + da

print("Basic Salary:", basic)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("Gross Salary:", gross_salary)