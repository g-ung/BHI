# Author: G Ung
# Date: Friday 18 May 2018
# Version: 3.0
#
# Rock Paper Scissors game - ask players to input names; #computer will compare 9 permutations to determine winner
# Two Players

# Ask for input from players 1 and 2
print("Welcome toi Rock, Paper, Scissors!")
print("Let's begin...")

name1 = str(input("Player 1: What's your name? "))
name2 = str(input("Player 2: What's your name? "))

print("Hello " + name1 + " and " + name2)
print(name2 + ": Close your eyes!")

choice1 = input(name1 + ": enter 'r' for rock, 'p' for paper, 's' for scissors: ")
print("Great choice! Now - cover your answer and ask " + name2 + " to choose. \n\n\n")
choice2 = input(name2 + ": enter 'r' for rock, 'p' for paper, 's' for scissors: ")

# Compare permutations for "R" scenario
if(choice1 == choice2):
    print(name1 + ": " + choice1 + " vs. " + name2 + ": " + choice2 + ", it is a draw")
elif(choice1 == "r"):
    if(choice2 == "s"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ": " + ", " + name1 + " wins")
    else:
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name2 + " wins")
elif(choice1 == "r"):
    if(choice2 == "p"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name2 + " wins")
elif(choice1 == "s"):
    if(choice2 == "r"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name2 + " wins")
    else:
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name1 + " wins")
elif(choice1 == "s"):
    if(choice2 == "p"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name1 + " wins")
# Compare permutations for "P" scenario
elif(choice1 == "p"):
    if(choice2 == "r"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name1 + " wins")
    else:
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name2 + " wins")
elif(choice1 == "p"):
    if(choice2 == "s"):
        print(name1 + ": " + choice1 + " vs. " + name2 +
              ": " + choice2 + ", " + name2 + " wins")
print("Thanks for playing Rock, Paper, Scissors")
