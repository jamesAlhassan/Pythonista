#!/usr/bin/python3

import os
from art import logo

print(logo)

def clear():
    os.system('clear')

print("Welcome to the secret auction program\n")
again = True
bidders = {}

while again:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid

    more_bidders = input("Are there other bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == 'yes':
        clear()
    elif more_bidders == "no":
        again = False
    else:
        print("Please enter 'yes'or 'no'")
winner = max(bidders, key=bidders.get)
print(f"The winner is {winner} with a bid of ${bidders[winner]}")
