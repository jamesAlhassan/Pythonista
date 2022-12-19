#!/usr/bin/python3


from art import logo, vs
from game_data import data
from random import randint as rd
import os


def clear():
    os.system('clear')


A = rd(0, len(data)) - 1
B = rd(0, len(data)) - 1

choice_A = data[A]
details_A = []

choice_B = data[B]
details_B = []

print(logo)

for k, v in choice_A.items():
    details_A.append(v)


print(f"Compare A: {details_A[0]}, {details_A[2]}, from {details_A[3]}")

print(vs)

for k, v in choice_B.items():
    details_B.append(v)

print(f"Against B: {details_B[0]}, {details_B[2]}, from {details_B[3]}")

more_followers = input("Who has more followers? Type 'A' or 'B': ")

score = 0
final_score = 0
if more_followers == 'A' and details_A[1] > details_B[1]:
    clear()
    score += 1
    final_score += 1
    print(f"You're right! Current score: {score}")

elif more_followers == 'B' and details_A[1] < details_B[1]:
    clear()
    score += 1
    final_score += 1
    print(f"You're right! Current score: {score + 1}")
else:
    print(f"Sorry, that's wrong. Final score: {final_score}")
