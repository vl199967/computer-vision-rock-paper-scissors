import random
from random import input

def get_computer_choice():
    options = ["Rock","Paper","Scissor","Nothing"]
    chose = random.choice(options)
    return chose 

def get_user_choice():
       user_choice = input()
       return user_choice

       