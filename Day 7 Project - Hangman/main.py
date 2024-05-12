import random
from hangman_art import *
from hangman_words import *

# Print out the hangman logo
print(hangman)

# Print message
print("\n Here's how to play: ")
print("\n1. You'll be presented with a random word, represented by a series of blanks.")
print(
    "\n2. Guess a letter. If it's correct, the blanks will be filled in with that letter."
)
print(
    "\n3. If your guess is incorrect, you'll lose a life. You have a total of six lives."
)
print("\n4. If you lose all your lives, the game is over and you lose. ")
print(
    "\n5. If you successfully fill in all the blanks, the word will be revealed and you win the game."
)
print("\n Good luck! \n")

# Empty list called display
display = []

# Choose a word randomly using random.choice function within the random module to choose a word from the list randomly

random_word = random.choice(word_list)
# print(random_word)

# The user starts with 6 lives.
lives = 6

# Pass _ into display list python in a iteration until the last word is checked.

for letter in random_word:
    display += "_"

# We assume that the hangman game is running
hangman_game_running = True

# Store a set of characters the user already guessed.
guessed_letters = set()

while hangman_game_running:

    # It loops through the condition until there isn't any blanks left in the display list
    if "_" in display:

        # Ask the user to guess a letter
        user_guess = input("Guess a letter: ")

        # If the the letter that the user guessed is not used, it executes the for loop and checks for a match.
        if user_guess not in guessed_letters:
            if user_guess in random_word:
                # Iterates each letter in the random word using range function to loop through between 0 and the end of the random word.
                for position in range(len(random_word)):
                    # It will assign the letter from random_word at position 0 to a variable called letter.
                    letter = random_word[position]
                    # If user's guess matches with the current letter within the position of the random word
                    if letter == user_guess:
                        # Replace the "_" at the current position with the user guess
                        display[position] = letter
                        print(display)
                        guessed_letters.add(user_guess)

            # At each turn if the guess is wrong, they lose a life.
            else:
                lives -= 1
                print(
                    f"You guessed `{user_guess}, that is not in the word. You lose a life"
                )
                # Print current stage which corresponds to the number of lives.
                print(stages[lives])
                guessed_letters.add(user_guess)

                # The player lost all the lives which means it sets hangman_game running to false and exits the loop
                if lives == 0:
                    print("You Lose!!")
                    hangman_game_running = False
        else:
            print(f"You've already guessed the letter {user_guess}")

    else:
        # Join the elements in the python list into one word and the game ends
        join_string = "".join(display)
        print(join_string)
        print("You win the game!!")
        hangman_game_running = False
