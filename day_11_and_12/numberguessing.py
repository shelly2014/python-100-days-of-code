# Added Features
# Ask user guess again if the input is not an integer
# Use black hearts to repreasent the attempts left
# Option to start another round
# Easy level - 10 attemps, range [1, 100]
# Medium level - 5 attemps, range [1, 100]
# Hard level - 5 attemps, range [1, 200]

import random
import os
from numberguessing_art import logo

def check_answer_correct(guess, answer):
    if guess == answer:
        print(f"You got it! The correct answer is {answer}!")
        return True
    elif guess < answer:
        print("The guess is too low. Please guess again..\n")
    else:
        print("The guess is too high. Please guess again..\n")
    return False

def print_attempts_left(attempts_left, attempts_total):
    print("Your attemps left: " + '❤ ' * attempts_left + "_ " * (attempts_total - attempts_left))

print(logo)
print("Welcome to the Number Guessing Game!")

game_on = True
while(game_on):
    level = input("Please choose a difficulty level.\nType 'e' for easy, 'm' for medium, or 'h' for hard: ")
    while level != 'e' and level != 'm' and level != 'h':
        level = input("Please choose a difficulty level.\nType 'e' for easy, 'm' for medium, or 'h' for hard: ")

    if level == 'e':
        attempts_total = 10
        attempts_left = 10
        max_range = 100
    elif level == 'm':
        attempts_total = 5
        attempts_left = 5
        max_range = 100
    else:
        attempts_total = 5
        attempts_left = 5
        max_range = 200

    answer = random.randint(1, max_range)
    print(f"You have {attempts_total} attempts. The correct answer is in the range of [1, {max_range}].\n")

    while attempts_left > 0 and game_on:
        print_attempts_left(attempts_left, attempts_total)
        guess = input("Please guess a number: ")
        if not guess.isdigit():
            print("Please guess an integer number.")
            continue
        guess = int(guess)

        if not check_answer_correct(guess, answer):
            attempts_left -= 1
        else:
            game_on = False

        if attempts_left == 0:
            print("Sorry you ran out of chance.")

    # Next round
    user_choice = input("\nType 'y' to start another round, type 'n' to exit: ").lower()
    if user_choice != 'y':
        game_on = False
    else:
        game_on = True
        os.system('cls')

print("\nThanks for playing the Number Guessing game. Bye.\n")