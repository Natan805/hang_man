


def show_hidden_word(secret_word, old_letters_guessed):
    """The function returns a string consisting of letters and underscores.
    The string displays the letters from the old_letters_guessed list
    that are in the secret_word string in their respective positions, and the rest of the letters in the
    return: str
    string (which the player has not yet guessed) as underscores."""

    result = ""
    for letter in secret_word:
        exists = False
        for old_letter_guessed in old_letters_guessed:

            if letter == old_letter_guessed:
                result += " " + letter
                exists = True
        if exists == False:
                result += " _ "

    return result




def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()

