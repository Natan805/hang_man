def is_valid_input(letter_guessed):
    """This function get the letter you guessed and give you the lengh of the character and also print you that as number with underscore
    it also check if its not vilid character like more then 1 letter so it print E1
    if its not valid like non-English character (for example, a sign such as: &, *)the string will print "E2
    the function print the letters just if it is one and english character
    :param letter_guessed : the letter you guessed
    :return the leter you guessed if it valid and E1 or E2 if its not valid
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

