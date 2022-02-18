# Author: G Ung
# Date: Friday 18 May 2018
# Version: 1.0
#
# Guess the random number game - ask player to input an integer
# between 1-6.  Computer will generate random number between 1-6 #and match your guess
# Player vs. Computer

import random
minGuess = 1
maxGuess = 6

# Ask the user for their name and their guess
name = str(input("What is your name?  "))
print("Hi " + name + "!")
print("Enter a number between: " + str(minGuess) + " and " + str(maxGuess))
guess = int(input("What is your guess? "))

# Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess, maxGuess)
if(guess == secretNumber):
    print("Congratulations, you got it right! " + str(secretNumber))
elif(guess != secretNumber):
    print("You lose, the number was " + str(secretNumber))
else:
    print("Thank you for playing the Guess the Number Game.")
