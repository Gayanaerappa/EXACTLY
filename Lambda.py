add = lambda a,b: a+b
print(add(10,5))
sub =lambda x,y: abs(x-y)
print(sub(40,30))
marks_diff = lambda m1,m2: abs(m1-m2)
print(marks_diff(50,65))
multi = lambda a,b: a*b
print(multi(100,2))
number = [1,2,3,4,5,6,7,8]
even_number = list(filter(lambda x: x%2==0,number))
print(even_number)