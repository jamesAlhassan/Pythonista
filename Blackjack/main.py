#!/usr/bin/python3


from art import logo
import random


# FUNCTIONS
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10, 10]
    return (random.choice(cards))


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

is_game_over = False
user_cards = []

computer_cards = []

for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)


print(user_score, computer_score)
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

