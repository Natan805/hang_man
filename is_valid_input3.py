def is_valid_input(letter_guessed):
    """This function get the letter you guessed and print true if its valid character with one letter and en English character
    but its print false if its invalid like more than one letter or non-English character (for example, a sign such as: &, *)
    :param letter_guessed : the letter you guessed
    :return true if it valid and false if its not valid
    :rtype str
    """

    #calulate the lengh of the letters
    NumberOfCharacters = (len(letter_guessed))
    #convert input letters to Underscore
    NumberOfUnderscore = (NumberOfCharacters * "_")


    # All the letters in English
    EnglishLetter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
    if NumberOfCharacters > 1:
        print("false")

    # If the user entered English character the string will print the character a non-English character (for example, a sign such as: &, *), the string will print "E2
    elif letter_guessed in EnglishLetter:
        print("true")
    else:
        print("false")

is_valid_input("app$")

