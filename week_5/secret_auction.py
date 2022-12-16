# Assign a bidder number to each bidder (bidders might have same name)
# Show the winner's bidder number instead of name
# If two bidders place the same bid, the leader will be the first one to have placed this bid.

import os
from art import logo
print(logo)

bids_record = []
def add_new_bid(name, bid_number, bid):
    record = {}
    record["name"] = name
    record["bid_number"] = bid_number
    record["bid"] = bid
    bids_record.append(record)

def find_winner(bids_record):
    max_bid = 0
    winner_number = 0
    for record in bids_record:
        if record["bid"] > max_bid:
            winner_number = record["bid_number"]
            max_bid = record["bid"]

    return [winner_number, max_bid]

continue_bid = True
bid_number = 1
while(continue_bid):
    print(f"Welcome to the secret auction program.\nYour bid number is {bid_number}")
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n$"))
    add_new_bid(name, bid_number, bid)
    bid_number += 1
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if more_bidders == "no":
        continue_bid = False
    os.system('cls')

winner = find_winner(bids_record)
print(f"The winner's bid number is {winner[0]} with a bid of ${winner[1]}!")
