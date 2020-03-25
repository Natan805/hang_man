#convert input to Underscore
InputUserWord = input("Please enter a word:")
NumberOfCharacters= (len(InputUserWord))
#All the letters in English
EnglishLetter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
#if the user insert more then 1 character printing E1
if NumberOfCharacters > 1 :
    alphabet = InputUserWord.isalpha()
    if alphabet == False :
        print("E3")
        exit()
    print("E1")
#If the user entered English character the string will print the character
elif InputUserWord in EnglishLetter:
    print(InputUserWord.lower())
#a non-English character (for example, a sign such as: &, *), the string will print the string "E2
else:
    print("E2")
