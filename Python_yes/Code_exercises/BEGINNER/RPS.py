#import random module

import random

#ASCII art for RPS

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#variables

choices = [rock , paper , scissors]

#src code
while True:
    user_choice = int(input("Enter your choice! (0 for Rock, 1 for Paper, 2 for Scissors)\n: "))
    computer_choice = random.randint(0,2)
    if user_choice not in range(0,3):
        print("You chose an invalid number, you lose.")
    else:
        print(f"You chose {choices[user_choice]}\nComputer chose {choices[computer_choice]}")
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 2 and computer_choice == 0):
            print("You lose...")
        elif (user_choice == 0 and computer_choice == 2):
            print("You win! :D")
        elif (user_choice < computer_choice):
            print("You lose...")
        elif (user_choice > computer_choice):
            print("You win! :D")
    continue_game = input("Type X to stop playing and Y to continue: ")
    if continue_game in "Xx":
        break