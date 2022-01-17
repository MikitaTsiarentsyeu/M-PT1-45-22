import random

x = random.randint(0, 10)

answer = int(input("Guess my number:"))

if answer == x:
    print("Correct!")
else:
    print("Looser!")