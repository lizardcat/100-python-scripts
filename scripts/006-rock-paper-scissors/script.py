# A simple rock, paper, scissors game

import random
import sys

rock = 0
scissors = 0
paper = 0
tie = 0
win = 0
lose = 0

print("Let's play rock, paper, scissors!")
print("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' for quit!")

userChoice = str(input())

if userChoice == "q":
    sys.exit
elif userChoice == "r":
    rock += 1
elif userChoice == "p":
    paper += 1
elif userChoice == "s":
    scissors += 1

botChoice = random.randint(1, 3)
