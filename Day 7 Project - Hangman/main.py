import random

# Create a Word list using Python lists

word_list = ["canada", "ghana", "germany"]

# Empty list called display
display = []

# Choose a word randomly using random.choice function within the random module to choose a word from the list randomly

random_word = random.choice(word_list)

# Pass _ into display list python in a iteration until the last word is checked.

for letter in random_word:
    display += "_"


# Ask the user to guess a letter
user_guess = input("Guess a letter: ")

# Initialized at position 0
position = 0

# Iterates each letter in the random word
for check_letter in random_word:
    # If user's guess matches with current letter in the random word
    if check_letter in user_guess:
        # Replace the "_" at the current position with the user guess
        display[position] = user_guess
    else:
        print("Incorrect letter")

    # Move to the next position on the display list
    position += 1

print(display)
