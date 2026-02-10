num = int(input("Enter a number: "))

if num >= 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Negative number")
