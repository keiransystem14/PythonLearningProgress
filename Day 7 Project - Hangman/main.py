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

# Iterates each letter in the random word using range function to loop through between 0 and the end of the random word.
for position in range(len(random_word)):
    # It will assign the letter from random_word at position 0 to a variable called letter.
    letter = random_word[position]
    # If user's guess matches with the current letter within the position of the random word
    if letter == user_guess:
        # Replace the "_" at the current position with the user guess
        display[position] = letter

print(display)
