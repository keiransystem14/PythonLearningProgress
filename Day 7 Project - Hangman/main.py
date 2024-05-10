import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

# Create a Word list using Python lists

word_list = ["canada", "ghana", "germany"]

# Empty list called display
display = []

# Choose a word randomly using random.choice function within the random module to choose a word from the list randomly

random_word = random.choice(word_list)

# The user starts with 6 lives.
lives = 6

# Pass _ into display list python in a iteration until the last word is checked.

for letter in random_word:
    display += "_"

# We assume that the hangman game is running
hangman_game_running = True

while hangman_game_running:

    # It loops through the condition until there isn't any blanks left in the display list
    if "_" in display:

        # Ask the user to guess a letter
        user_guess = input("Guess a letter: ")

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

        # At each turn if the guess is wrong, they lose a life.
        else:
            lives -= 1
            # Update the current stage based on the number of incorrect guesses
            current_index = min(lives, len(stages) - 1)
            # Print current stage
            print(stages[current_index])

        if lives == 0:
            print("You Lose!!")
            hangman_game_running = False

    else:
        # Join the elements in the python list into one word
        join_string = "".join(display)
        print(join_string)
        print("You win the game!!")
