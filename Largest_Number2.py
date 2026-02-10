nums = [10, 45, 78, 23, 56, 89, 12]

first = second = third = float('-inf')

for n in nums:
    if n > first:
        third = second
        second = first
        first = n
    elif n > second and n != first:
        third = second
        second = n
    elif n > third and n != first and n != second:
        third = n

print("Third largest number:", third)