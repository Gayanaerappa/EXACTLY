sentence = "Python is very easy to learn and Python is powerfull"
words = sentence.split()
dic ={}
for w in words:
    if w in dic:
        dic[w] += 1
    else:
        dic[w] = 1
    print(w,":",dic[w])        

