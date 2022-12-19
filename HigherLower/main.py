#!/usr/bin/python3


from art import logo, vs
from game_data import data
from random import randint as rd
import os


def clear():
    os.system('clear')

score = 0
final_score = 0


correct = True

while correct:
    A = rd(0, len(data)) - 1
    B = rd(0, len(data)) - 1
    
    if A == B:
        B +=1

    choice_A = data[A]
    choice_B = data[B]


    details_A = []
    details_B = []
    
    print(logo)
    
    for k, v in choice_A.items():
        details_A.append(v)
    
    
    print(f"Compare A: {details_A[0]}, {details_A[2]}, from {details_A[3]}")
    
    print(vs)
    
    for k, v in choice_B.items():
        details_B.append(v)
    
    print(f"Against B: {details_B[0]}, {details_B[2]}, from {details_B[3]}")
    
    followers =  input("Who has more followers? Type 'A' or 'B': ")
    

    if followers == 'A' and details_A[1] > details_B[1]:
        clear()
        score += 1
        final_score += 1
        print(f"You're right! Current score: {score}")
        details_B = details_A
        
    
    elif followers == 'B' and details_A[1] < details_B[1]:
        clear()
        score += 1
        final_score += 1
        print(f"You're right! Current score: {score}")
        details_B = details_A
    else:

        print(f"Sorry, that's wrong. Final score: {final_score}")
        correct = False
