#!/usr/bin/python3


from art import logo, vs
from game_data import data
from random import randint as rd

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
