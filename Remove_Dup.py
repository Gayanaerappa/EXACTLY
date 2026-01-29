number = [1,2,2,3,4,5,5,6,7,7,8,9,10]
unique =[]
for i in number:
    if i not in unique:
        unique.append(i)
print("the original Number",number)        
print("After the removing the duplicates numnber:",unique)        