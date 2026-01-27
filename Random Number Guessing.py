import random

secret = random.randint(1, 5)

guess = int(input("Guess a number between 1 and 5: "))

if guess == secret:
    print("Correct Guess")
else:
    print("Wrong Guess")
    print("Number was:", secret)