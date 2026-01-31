sentence = input("Enter a sentence: ")
words = sentence.split()

print("Words are:")
for w in words:
    print(w)

print("Word Count:", len(words))