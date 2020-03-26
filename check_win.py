

def check_win(secret_word, old_letters_guessed):
    """
    The function returns True if all the letters that make up the secret word are included in the list
    of letters the user guessed. Otherwise, the function returns False.
    return: bool
    """
    from show_hidden_word import show_hidden_word

    result = show_hidden_word(secret_word, old_letters_guessed)
    if "_" in result:
        return False
    else:
        return True


def main():
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == "__main__":
    main()

