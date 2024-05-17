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


def encrypt(plain_text, forward_shift):

    # Empty python list
    encrypted_string = []

    # It iterates through the text the user has inputted
    for position in range(0, len(plain_text)):

        # Starts going through the text by each character.
        letter_check = plain_text[position]

        # It iterates through the alphabet in order.
        for alpha_check in alphabet:

            # It checks if the character from the text is the same as the character in the alphabet.
            if alpha_check == letter_check:

                # It the position of the letter inside the alphabet python list using the index() function.
                index = alphabet.index(alpha_check)

                # Shifts each letter in the text forwards as part of encrypting the text.
                new_position = index + forward_shift

                # Adds the a new letter within the index of the new position into empty python list
                encrypted_string += alphabet[new_position]

    # Combines all the letters into one word to complete the encrypted message.
    encrypted_message = "".join(encrypted_string)

    # prints the enrcrypted message
    print(f"The encoded text is: {encrypted_message}")


def decrypt(encoded_text, backward_shift):

    # Empty python list
    decrypt_string = []

    # It iterates through the text the user has inputted
    for position in range(0, len(encoded_text)):

        # Starts going through the text by each character.
        letter_check = encoded_text[position]

        # It iterates through the alphabet in order.
        for alpha_check in alphabet:

            # It checks if the character from the text is the same as the character in the alphabet.
            if alpha_check == letter_check:

                # It the position of the letter inside the alphabet python list using the index() function.
                index = alphabet.index(alpha_check)

                # Shifts each letter in the text backwards as part of decrypting the text.
                new_position = index - backward_shift

                # Adds the a new letter within the index of the new position into empty python list
                decrypt_string += alphabet[new_position]

    # Combines all the letters into one word to complete the encrypted message.
    decrypt_message = "".join(decrypt_string)

    # prints the enrcrypted message
    print(f"The decoded text is: {decrypt_message}")


# Checks if the user wanted to encrypt or decrypt by checking the directon variable with IF statements.

if direction == "encode":
    encrypt(plain_text=text, forward_shift=shift)
elif direction == "decode":
    decrypt(encoded_text=text, backward_shift=shift)
else:
    print("This option doesn't exist.")
