# Author: G Ung
# Date: Friday 18 May 2018
# Version: 1.0
#
# Guess the random number game - ask player to input an integer
# Computer will generate random number between 1-20 and match your guess
# Player vs. Computer

import random

secret_num = random.randint(1, 20) # Generate random number between 1-20

# Ask the user for their name
name = str(input("What is your name?  "))
print("Hi {}!\n".format(name))
print("I am thinking of a number between 1 and 20.\n")

# Ask player to guess the secret number, max guesses: 6
for guesses in range(1, 7):
    print("What is your guess?  You have 6 guesses.")
    guess = int(input())
    if guess < secret_num:
        print("Your guess is too low, try again.")
    elif guess > secret_num:
        print("Your guess is too high, try again.")
    else:
        break # Guess is neither too high or low, therefore condition is correct guess

if guess == secret_num:
    print("Congratulations, you got it right! {} was the secret number. You guessed the number in {} guesses!".format(secret_num, guesses))
else:
    print("You lose, the number was {}. Thank you for playing the Guess the Number Game.".format(secret_num))