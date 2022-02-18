# Author: G Ung
# Date: Sunday 20 May 2018
# Version: 1.0
#
# Math Quest: helping students to practice their times table
# from 1-12.  Program will display answers as student practice
# on piece of paper

# Ask user to input their name
name = str(input("Welcome to Math Quest! Please enter your name: "))
timesTable = int(
    input("Hello " + name + ", which times table would you like to practice? (1-12): "))
print("Okay " + name + ": on a piece of paper, write down the " + str(timesTable) +
      " times table from 1 to 12.  When you're ready I'll show you the answers so you can check you work \n")

start = str(input("Are you ready? (Enter 'Y' to start): "))

# Calculate times table using range
total = int(0)
while(start == "n"):
    start = str(input("Are you ready? (Enter 'Y' to start): "))
if(start == "y"):
    for i in range(1, 13):
        total = timesTable * i
        print(str(i), " x ", str(timesTable) + " = ", str(total))

# Ask student if they got it right
correct = str(input("Did you get them all correct? (y/n): "))
if(correct == "y"):
    print("Great job! Thank you for playing Math Quest")
else:
    print("No? Better luck next time")
