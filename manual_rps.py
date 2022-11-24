import random
from random import input

def get_computer_choice():
    options = ["rock","paper","scissor","nothing"]
    chose = random.choice(options)
    return chose 

def get_user_choice():
       user_choice = input()
       return user_choice

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice :
        print("It's a tie!")
    if (computer_choice == "paper" and user_choice == "scissor") or (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "scissor" and user_choice == "rock"): 
        print("You won!")
    else:
        print("You lost!")                        