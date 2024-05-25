from art import *
import os

print(auction_title + "\n")

# Print Auction Logo
print(auction_logo + "\n")

# User Bidders Dictionary which is currently empty
user_bidders = {}

# Auction does continue until there is no additional bidders who want to bid.
Continue_Auction = True


# Create a function called highest bidder with a variable inside parameter called bid_database
def highest_bidder(bid_database):
    # Current highest bid is 0
    highest_bid = 0
    # String value to append the user who has the highest bid.
    bid_winner = ""

    # The for loop iterates through all the enteries inside the user_bidders dictionary. For each entry, it checks if the bid amount is higher than the highest bid so far. If it is, the highest bid and corrosponding user identifed are updated. By the end of the loop the highest_bid variable contains the highest bid and the bid_winner variable contains the name of the person with the highest bid.
    for user_bid in bid_database:
        bid_amount = bid_database[user_bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bid_winner = user_bid
    print(f"The winner is {bid_winner} with a bid of £{highest_bid}")


while Continue_Auction:
    # Requesting for user details that are bidding using input()
    name = input("What is your name?: ")
    bid_price = int(input("What's your bid price?: "))

    # Add the output of name as the key and output of bid_price as the value in the user_bidders dictionary
    user_bidders[name] = bid_price
    should_continue = input("Are there any other bidders?: ")

    # If there are other bidders, it will continue to go through the while loop. Otherwise the Auction will end and print out the name that is the highest bidder
    if should_continue == "yes":
        os.system("clear")
    elif should_continue == "no":
        Continue_Auction = False
        highest_bidder(user_bidders)
