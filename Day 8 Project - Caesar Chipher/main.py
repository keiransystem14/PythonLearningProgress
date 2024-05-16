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

                print(index)


encrypt(text, shift)
