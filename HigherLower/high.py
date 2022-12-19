#!/usr/bin/python3


from art import logo, vs
from game_data import data
from random import choice as ch
import os


def clear():
    os.system('clear')
def get_random_account():
  """Get data from random account"""
  return ch(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  des = []
  for k, v in account.items():
      des.append(v)
  return f"{des[0]}, a {des[2]}, from {des[3]}"


def check_followers(account):
    des = []
    for k, v in account.items():
        des.append(v)
    return f"{des[1]}"
    
    
    
def check_answer(guess, choice_A, choice_B):
    if guess == "A" and choice_A > choice_B:
        return True
    elif guess == "B" and choice_B > choice_A:
        return True
    else:
        return False


def game():
  print(logo)
  score = 0
  game_should_continue = True
  choice_A = get_random_account()
  choice_B = get_random_account()

  while game_should_continue:
    choice_A = choice_B
    choice_B = get_random_account()
    
    while choice_A == choice_B:
        choice_B = get_random_account()

    print(f"Compare A: {format_data(choice_A)}.")
    print(vs)
    print(f"Against B: {format_data(choice_B)}.")
    
    more_followers = input("Who has more followers? Type 'A' or 'B': ").upper()
    is_correct = check_answer(more_followers, check_followers(choice_A), check_followers(choice_B))

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
