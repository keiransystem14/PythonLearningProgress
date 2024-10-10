import random
from os import remove


# Create a deal_card() function that uses the List below to return a random card.

def deal_card():

    #List of cards in the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Choose a card randomly from the cards list
    card = random.choice(cards)
    return card

# Users hand
user_cards = []
# Computers hand
computer_cards = []

user_cards.append(deal_card())
computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)

def calculate_score(cards):

    # List of cards as input and returns the sum of all the cards in the List as the score.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Check for Ace and if the score goes over 21 with an Ace, it replaces the 11 with the 1.
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


#def compare():



