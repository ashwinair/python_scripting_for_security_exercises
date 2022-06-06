# write a short command line game

# 1. ask the user for their name: (use the input() function)
name = input("Enter your name: ")
# Say hello to them with their name
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
# If their name begins with a consonant make an even better joke about it.
if name[0].lower() == 'a' or name[0].lower() == 'i' or name[0].lower() == 'e' or name[0].lower() == 'o' or name[
    0].lower() == 'u':
    print(f"Aha!, your name begins with a vowel, HELLO {name}")
else:
    print(f"Hmmm.. not your name not begins with a vowel btw hello {name}")
# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.
no = input("can you guess a no between 1 and 10: ")

import random

random_number = random.randint(0, 10)

if no == random_number:
    print("nice guess")
else:
    print("aah, bad luck")
