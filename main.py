print("Random number guessing from 1-1,000,000!!!")
import random

attempts = 1
mynumber = random.randint(1, 1000000)
while True:
    guess = int(input("What is your guess?"))
    if guess > mynumber:
        print("too high")
        attempts += 1
    elif guess < mynumber:
        print("too low")
        attempts += 1
        continue
    elif guess == mynumber:
        print("congrats on finally winning.")
        break
        exit()
    else:
        print("No negatives...")
print("congrats on finally guessing correclty after", attempts, "attempts")
