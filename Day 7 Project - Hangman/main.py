import random

# Create a Word list using Python lists

word_list = ["brazil", "germany", "peru"]

# Choose a word randomly using random.choice function within the random module to choose a word from the list randomly

random_word = random.choice(word_list)
random_word.split()


# Ask the user to guess a letter

user_guess = input("Guess a letter: ")

# Blank words
blank_list = []

# It scans through each letter in the word to see if it matches with the user guess. If it does, it would pass the user guess into a blank word python list and print out correct letter. If user guess is incorrect, it will print out incorrect letter.
# This will be done in a iteration until all the letters in the word have been checked.
for check_word in random_word:
    if check_word == user_guess:
        blank_list.append(user_guess)
        print("Correct letter")

    else:
        print("Incorrect letter")
