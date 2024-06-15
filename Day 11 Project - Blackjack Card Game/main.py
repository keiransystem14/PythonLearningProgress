import random

# Current hand is empty
user = []
computer = []

# Type of cards.
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():

    # Number of cards to start with
    hand_size = 2

    # Iterates the loop two times until both user and computer recieves two cards
    for _ in range(hand_size):

        # It chooses generates a card in random and passes it over to user and computer list.
        user.append(random.choice(cards))
        computer.append(random.choice(cards))


def calculate_score():

    # Program accessing the users hand.
    user_first_hand = user[0]
    user_second_hand = user[1]

    # Progran acccessubg the computer's hand.
    computer_first_hand = computer[0]
    computer_second_hand = computer[1]

    # Total score for user
    user_total_score = user_first_hand + user_second_hand

    # Total score for computer
    computer_total_score = computer_first_hand + computer_second_hand

    # Checks if user has a 10 on their hand and Ace card which is 11 on their hand.
    if 10 in user and 11 in user:
        print("User Wins!!")
    # Checks if computer has a 10 card and Ace card which is 11 on their hand.
    elif 10 in computer and 11 in computer:
        print("User Lose!!")
    else:
        print("There's no blackjack!!")
        # Checks if the score is over 21
        if user_total_score > 21:
            if 11 in user:
                user_total_score += 1
                print(user_total_score)

            else:
                print("You Lose!!")
        else:
            another_card = input("Do you want to get another card?").lower()

            if another_card == "yes":
                user.append(random.choice(cards))
            elif another_card == "no":
                if computer_total_score < 17:
                    computer.append(random.choice(cards))
                    computer_total_score += computer[2]
                else:
                    if computer_total_score > 21:
                        print("You win!!")

            print(f"User total score is {user_total_score}")
            print(f"Computer total score is {computer_total_score}")

            if computer_total_score > user_total_score:
                print("You Lose!!")
            elif computer_total_score < user_total_score:
                print("You Win!!")
            else:
                print("You Draw!!")


deal_cards()
calculate_score()
