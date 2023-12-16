import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

user_deck = []
computer_deck = []

end_game = False

while not end_game:
    flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if flag == 'n':
        end_game = True
    else:
        os.system('cls')
        for i in range(2):
            user_deck.append(random.choice(cards))
        dealer_1 = random.choice(cards)
        computer_deck.append(dealer_1)