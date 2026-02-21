marks =[]
n = int(input("How many student?"))
for i in range (n):
    m = int(input(f"Enter marks for student{i+1}:"))
    marks.append(m)
total = sum(marks)  
average = total / n
highest = max(marks)
lowest= min(marks)
print("\n======Result======")
print("total Marks",total)
print("average marks", average)
print("highest marks",max)
print("lowest marks",min)
  #count pass/ fail
pass_count = 0
fail_count =0
for m in marks:
    if m >= 40:
        pass_count+=1  
    else:
        fail_count +=1
print("passed",pass_count) 
print("failed",fail_count)       