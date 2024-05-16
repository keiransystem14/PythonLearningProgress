alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):

    encrypted_string = []

    # It iterates through the text the user has inputted
    for position in range(0, len(text)):

        # Starts going through the text by each character.
        letter_check = text[position]

        # It iterates through the alphabet in order.
        for alpha_check in alphabet:

            # It checks if the character from the text is the same as the character in the alphabet.
            if alpha_check == letter_check:

                # It the position of the letter inside the alphabet python list using the index() function.
                index = alphabet.index(alpha_check)

                # Shifts each letter in the text forwards as part of encrypting the text.
                new_position = index + shift

                # Adds the a new letter within the index of the new position into empty python list
                encrypted_string += alphabet[new_position]

    # Combines all the letters into one word to complete the encrypted message.
    encrypted_message = "".join(encrypted_string)

    # prints the enrcrypted message
    print(encrypted_message)


# Executes the function called encrypt with two inputs - text and shift
encrypt(text, shift)
