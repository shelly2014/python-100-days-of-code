# Added Features
# Created card symbols with ascii art
# Print the dealer's 2nd card as blind card at the player's round
# Use a dictionary to store card values
# Address multiple 'A's situation since the deck is unlimited in size
# Pause 1.5s after dealer draw each card and update the card status
# If the player busts, the dealer will not hit his hand, no matter what he has.


## Rules defined by the Udemy course
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## The dealer must stand on 17 or higher

import random
import os
import time
import copy
from blackjack_art import logo
from blackjack_art import CARD_SYMBOLS

CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_VALUES = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

def draw_card(num):
    cards = []
    for i in range(0, num):
        cards += random.sample(CARDS, 1)
    return cards

def print_cards(cards):
    for line_num in range(0, 6):
        line = []
        for card in cards:
            line += CARD_SYMBOLS[card][line_num]
        print("".join(line))

def print_cards_2nd_hidden(cards):
    cards_2nd_hidden = copy.deepcopy(cards)
    # '0' stands for hidden card
    cards_2nd_hidden[1] = '0'
    print_cards(cards_2nd_hidden)

def get_cards_vaule(cards):
    cards_value = 0
    for card in cards:
        cards_value += CARD_VALUES[card]
    # Update the value if necessary
    countA = cards.count('A')
    if(cards_value > 21):
        for i in range(0, countA):
            cards_value -= 10
            if (cards_value <= 21):
                break
    return cards_value

def print_status_player_turn_on(dealer_cards, player_cards):
    print("---♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣---")
    print("\n-------------Dealer's Cards-------------")
    print_cards_2nd_hidden(dealer_cards)
    print("\n---------------Your Cards---------------")
    print_cards(player_cards)
    player_score = get_cards_vaule(player_cards)
    print(f'Your value: {player_score}\n')

def print_status_dealer_turn_on(dealer_cards, player_cards):
    print("---♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣---")
    print("\n-------------Dealer's Cards-------------")
    print_cards(dealer_cards)
    dealer_score = get_cards_vaule(dealer_cards)
    print(f"Dealer's value: {dealer_score}")
    print("\n---------------Your Cards---------------")
    print_cards(player_cards)
    player_score = get_cards_vaule(player_cards)
    print(f'Your value: {player_score}\n')

def player_turn(dealer_cards, player_cards):
    player_turn_on = True
    while(player_turn_on):
        player_choice = input("Type 'h' to hit or 's' to stand: ").lower()
        if player_choice == 's':
            player_turn_on = False
        elif player_choice == 'h':
            os.system('cls')
            player_cards += draw_card(1)
            print_status_player_turn_on(dealer_cards, player_cards)
            player_score = get_cards_vaule(player_cards)
            if(player_score >= 21):
                player_turn_on = False

def dealer_turn(dealer_cards, player_cards):
    dealer_turn_on = True
    while(dealer_turn_on):
        os.system('cls')
        dealer_cards += draw_card(1)
        print_status_dealer_turn_on(dealer_cards, player_cards)
        dealer_score = get_cards_vaule(dealer_cards)
        if(dealer_score >= 17):
            dealer_turn_on = False
        time.sleep(1.5)

def check_result(dealer_cards, player_cards):
    os.system('cls')
    print_status_dealer_turn_on(dealer_cards, player_cards)

    player_score = get_cards_vaule(player_cards)
    dealer_score = get_cards_vaule(dealer_cards)

    if(player_score == dealer_score):
        print("Same score. Draw.")
    elif(player_score == 21):
        print("You got a BLACKJACK! You win!!")
    elif(dealer_score == 21):
        print("Sorry dealer got a BLACKJACK.. you loose..")
    elif(player_score > 21):
        print("Sorry you busted.. you lose..")
    elif(dealer_score > 21):
        print("Dealer busted! You win!! ")
    elif(player_score < dealer_score):
        print("Sorry dealer got a higher score.. you loose..")
    else:
        print("You got a higher score! You win!! ")

# Start
print(logo)
user_choice = input("\nType 'y' to start the BLACKJACK game, type 'n' to exit: ").lower()
if user_choice != 'y':
    game_on = False
else:
    game_on = True

while(game_on):
    # Dealer and player start with 2 random cards
    dealer_cards = draw_card(2)
    player_cards = draw_card(2)
    print_status_player_turn_on(dealer_cards, player_cards)

    # Player's turn
    player_score = get_cards_vaule(player_cards)
    if(player_score != 21):
        player_turn(dealer_cards, player_cards)

    # Dealer's turn
    player_score = get_cards_vaule(player_cards)
    dealer_score = get_cards_vaule(dealer_cards)
    if(player_score <= 21 and dealer_score < 17):
        dealer_turn(dealer_cards, player_cards)

    # Check result
    check_result(dealer_cards, player_cards)

    # Next round
    print("---♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣---")
    user_choice = input("\nType 'y' to start another round, type 'n' to exit: ").lower()
    if user_choice != 'y':
        game_on = False
    else:
        os.system('cls')

print("\nThanks for playing the BLACKJACK game. Bye.\n")
print("---♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣-----♠-♦-♥-♣---")

