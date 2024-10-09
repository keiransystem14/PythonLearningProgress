import random


# Create a deal_card() function that uses the List below to return a random card.

def deal_card():

    #List of cards in the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Choose a card randomly from the cards list
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

user_cards.append(deal_card())
computer_cards.append(deal_card())

print(user_cards)
print(computer_cards)
#def compare():

#def calculate_score():

