import random

def get_computer_choice():
    options = ["Rock","Paper","Scissors"]
    chose = random.choice(options)
    return chose 

def get_user_choice():
       user_choice = input("rock paper scissor!")
       return user_choice

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice :
        print("It is a tie!")
    if (computer_choice == "Paper" and user_choice == "scissor") or (computer_choice == "Rock" and user_choice == "paper") or (computer_choice == "Scissors" and user_choice == "rock"): 
        print("You won ")
    else:
        print("You lost")                       


def play():
    playa = get_user_choice()
    comp = get_computer_choice()
    get_winner(comp,playa)

play()           