


def show_hidden_word(secret_word, old_letters_guessed):
    result = ""
    for letter in secret_word:
        exists = False
        for old_letter_guessed in old_letters_guessed:

            if letter == old_letter_guessed:
                result += letter
                exists = True
                print(exists)
        print(exists)
        if exists == True:
                result += "_ "

    print(result)
secret_word = "m"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
show_hidden_word(secret_word, old_letters_guessed)
