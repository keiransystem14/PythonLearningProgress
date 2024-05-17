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


def caesar(direction, text, shift):

    encoded_string = []
    plaintext_string = []

    # Checks if the user wanted to encrypt or decrypt by checking the directon variable with IF statements.
    if direction == "encode":

        for position in range(0, len(text)):

            # Starts going through the text by each character.
            letter_check = text[position]

            # It iterates through the alphabet in order.
            for alpha_check in alphabet:

                # It checks if the character from the text is the same as the character in the alphabet.
                if alpha_check == letter_check:

                    # It the position of the letter inside the alphabet python list using the index() function.
                    index = alphabet.index(alpha_check)

                    # Shifts each letter in the text forwards as part of encrypting the text. Also to ensure it stays within the range of alphabets.
                    new_position = (index + shift) % len(alphabet)

                    # Adds the a new letter within the index of the new position into empty python list
                    encoded_string += alphabet[new_position]

        # Combines all the letters into one word to complete the encrypted message.
        encrypted_message = "".join(encoded_string)

        # prints the enrcrypted message
        print(f"The {direction} text is: {encrypted_message}")

    elif direction == "decode":

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

                    # Shifts each letter in the text backwards as part of decrypting it into plain text. Also to ensure it stays within the range of alphabets.
                    new_position = (index - shift) % len(alphabet)

                    # Adds the a new letter within the index of the new position into empty python list
                    plaintext_string += alphabet[new_position]

        # Combines all the letters into one word to complete the decrypting encoded text into plain text.
        decrypt_message = "".join(plaintext_string)

        # prints the enrcrypted message
        print(f"The {direction} text is: {decrypt_message}")
    else:
        print("This option doesn't exist.")


# Call caesar function with parameters to execute the function.
caesar(direction, text, shift)
