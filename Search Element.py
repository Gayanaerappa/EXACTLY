numbers = [10,20,30,40,50]
Key =int(input("Enter the number:"))
found = False
for n in numbers:
    if n == Key:
        found = True
        break
if found:
    print("number Found!")
else:
    print("number not found")        