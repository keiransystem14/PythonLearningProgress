import random
from os import remove


# Create a deal_card() function that uses the List below to return a random card.
def deal_card():

    #List of cards in the deck.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Choose a card randomly from the cards list
    card = random.choice(cards)
    return card


def calculate_score(cards):

    # List of cards as input and returns the sum of all the cards in the List as the score.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Check for Ace and if the score goes over 21 with an Ace, it replaces the 11 with the 1.
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)

    # It returns the total score of the cards.
    return sum(cards)

def play_game():

    # Users hand
    user_cards = []
    # Computers hand
    computer_cards = []

    # It gives two cards to Computer and user.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calculates the user total score
    print(f"Your cards: {user_cards}, current score: {calculate_score(cards=user_cards)}.")
    print("Computer's First card is:", user_cards[0])

    multiple_cards = True

    while multiple_cards:

        another_card = input("Type 'yes' to get another card or 'no' to pass: ")

        if another_card == "yes":
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, current score: {calculate_score(cards=user_cards)}.")
            print("Computer's First card is:", user_cards[0])
        elif another_card == "no":
            print(f"Your final hand: {user_cards}, final score: {calculate_score(cards=user_cards)}.")
            print(f"Computer's hand: {computer_cards}, final score: {calculate_score(cards=computer_cards)}.")
            multiple_cards = False

play_game()

#def compare():



