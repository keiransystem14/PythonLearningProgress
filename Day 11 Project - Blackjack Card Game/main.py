import random

# Current hand is empty
user = []
computer = []


def deal_cards():

    # Type of cards.
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Number of cards to start with
    hand_size = 2

    # Iterates the loop two times until both user and computer recieves two cards
    for _ in range(hand_size):

        # It chooses generates a card in random and passes it over to user and computer list. 
        user.append(random.choice(cards))
        computer.append(random.choice(cards))

def calculate_score():

    

deal_cards()
