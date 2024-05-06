import random

# Create a Word list using Python lists

word_list = ["brazil", "germany", "peru"]

# Choose a word randomly using random.choice function within the random module to choose a word from the list randomly

random_word = random.choice(word_list)
random_word.split()


# Ask the user to guess a letter

user_guess = input("Guess a letter: ")

blank_list = []

for check_word in random_word:
    if check_word == user_guess:
        blank_list.append(user_guess)
        print("Correct letter")

    else:
        print("Incorrect letter")
