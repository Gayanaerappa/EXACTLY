s = input("Enter the Paragraph:")
count =0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print("total number of vowel is:",count)        