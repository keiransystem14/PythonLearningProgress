from art import *
import os

# Print Auction Logo
print(auction_logo)

# Requesting for details
name = input("What is your name?: ")
bid_price = input("What's your bid price?: ")


def add_user_details(name1, new_bid_price):
    users = {}
    users[name1] = "Name"
    users[new_bid_price] = "Price"

    question = input("Are there any other bidders?: ")

    if question == "yes":
        os.system("clear")
    else:
        print("Winner of the Auction is")


add_user_details(name1=name, new_bid_price=bid_price)
