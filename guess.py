import random

guessesTaken = 0

print("Hello! What is your name?")
playerName = input()

number = random.randint(1, 20)
print("Well, " + playerName + " , I am thinking of a number between 1 and 20.")

for guessesTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is to low.")

    if guess > number:
        print("Your guess is to high.")
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + playerName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")