old_letters = ['a', 'b', 'c']

def check_valid_input(letter_guessed, old_letters_guessed):
    """This function get the letter you guessed and print true if its valid character with one letter and en English character
    but its print false if its invalid like more than one letter or non-English character (for example, a sign such as: &, *)
    or letter that you chosen before.
    :param letter_guessed : the letter you guessed
    :return true if it valid and false if its not valid
    :rtype str
    """

    # calculate the length of the letters
    number_of_characters = (len(letter_guessed))

    # convert input letters to underscore
    number_of_underscore = (number_of_characters * "_")
    print(number_of_underscore)

    # Check the letter is 1 Character and if the user entered English character the string
    # will print the character a non-English character (for example, a sign such as: &, *), the string will print "E2
    english_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    if number_of_characters > 1:
        return "false"
    elif letter_guessed in english_letter and letter_guessed not in old_letters_guessed:
        return "true"
    else:
        return "false"


if __name__ == "__main__ ":

    print(check_valid_input('c', old_letters))

