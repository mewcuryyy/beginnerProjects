import os
import logo

bidding = {}

auction_end = False

while not auction_end:
    print(logo.logo)
    print("Welcome to secret auction program!")
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    bidding[name]=bid
    run_again = input("Are there any other bidders? (yes/no): ")
    os.system('cls')
    if run_again == "no":
        max_bid = 0
        for key in bidding:
            if bidding[key] > max_bid:
                max_bid = bidding[key]
                max_bidder = key
        print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
        auction_end = True
        