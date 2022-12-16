# Added Features
# Re-draw if the two entries have same follower counts 
# Display the pair horizontally

from art import logo, vs
from game_data import data
import random
import os
import copy

NUM_ENTRY = len(data)

def draw_entry(entryA_count = None):
    entry = random.randint(0, NUM_ENTRY-1)
    # Re-draw if needed
    if entryA_count:
        while data[entry]['follower_count'] == entryA_count:
            entry = random.randint(0, NUM_ENTRY-1)
    return data[entry]

def print_entry(entryA, entryB):
    entry_key = ['name', 'country', 'description', 'follower_count']
    print("")
    for i in range(0, 3):
        line = []
        line += "{:<40}".format(entryA[entry_key[i]])
        line += vs[i]
        line += "{:<40}".format(entryB[entry_key[i]])
        print("".join(line))
    line = "{:<40}".format("Follower count: " + str(entryA[entry_key[3]]))
    line += vs[3]
    line += "{:<25}".format("Follower count: ░░░░")
    print("".join(line))
    print("")

def check_answer(entryA, entryB):
    line = "{:<58}".format("")
    line += (entryB['name'] + " has higher or lower follower count than " + entryA['name'] + "?")
    print("".join(line))
    answer = input("{:<58}".format("") + "Type 'h' for higher or 'l' for lower: ").lower()
    if(entryA['follower_count'] > entryB['follower_count']):
        correct_answer = 'l'
    else:
        correct_answer = 'h'
    if(answer == correct_answer):
        return True
    else:
        return False

print(logo)
print("The Higher Lower game - Instagram version")
user_choice = input("\nType 'y' to start the Higher Lower game, type 'n' to exit: ").lower()
if user_choice != 'y':
    new_game = False
else:
    new_game = True

while(new_game):
    score = 0
    entryA = draw_entry()
    entryB = draw_entry(entryA['follower_count'])  
    print_entry(entryA, entryB)
    game_on = True
    while(game_on):
        game_on = check_answer(entryA, entryB)
        if(game_on):
            score += 1
            print("{:<25}".format("") + f"You're right! Current score: {score}")
            entryA = copy.deepcopy(entryB)
            entryB = draw_entry(entryA['follower_count'])
            print_entry(entryA, entryB)
        else:
            print("{:<58}".format("") + f"The follower count of {entryB['name']} is {entryB['follower_count']}.")
            print("{:<25}".format("") + f"Sorry, you're wrong. Final score: {score}")
            score = 0
    
    # Next round
    user_choice = input("\nType 'y' to start another round, type 'n' to exit: ").lower()
    if user_choice != 'y':
        new_game = False
    else:
        new_game = True
        os.system('cls')
