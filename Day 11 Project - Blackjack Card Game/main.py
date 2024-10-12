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

#def compare():



def play_game():


    # Users hand
    user_cards = []
    # Computers hand
    computer_cards = []

    #User score
    user_score = -1

    #Computer score
    computer_score = -1

    game_over = False


    # It gives two cards to Computer and user.
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    """

        Create a while loop to demonstrate that if the user selects yes, it would go in a loop until the user says no. 
        If answer is no then the condition changes to false.

    """

    while not game_over:

        # Calculates the user total score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)


        print(f"Your cards: {user_cards}, current score: {user_score}.")
        print("Computer's First card is:", computer_cards[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'yes' to get another card or 'no' to pass: ")

            if user_should_deal == "yes":
                user_cards.append(deal_card())
            elif user_should_deal == "no":
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}.")
    print(f"Computer's hand: {computer_cards}, final score: {computer_score}.")


play = input("Do you want to play the game of Blackjack 'Yes' or 'No': ")

if play == "Yes".lower():
    play_game()



