import random
print ("""  _    _ 
 | |  | |
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")


print (random.randint(0, 10))

print("x-------x")
print("""x-------x
|
|
|
|
|""")
print("""x-------x
|       |
|       0
|
|
|""")
print("""x-------x
|       |
|       0
|       |
|
|""")
print("""x-------x
|       |
|       0
|      /|\\
|
|""")
print("""x-------x
|       |
|       0
|      /|\\
|      /
|""")
print("""x-------x
|       |
|       0
|      /|\\
|      / \\
|""")

#InputUser = input("Guess a letter:")
#print (InputUser.lower())
#####convert input to Underscore
InputUserWord = input("Please enter a word:")
NumberOfCharacters=  (len(InputUserWord))
NumberOfUnderscore = (NumberOfCharacters * "_" )
print (NumberOfUnderscore)


if NumberOfCharacters > 1 :
    print("E1")

#If the user entered English character th string will print the character  a non-English character (for example, a sign such as: &, *), the string will print the string "E2
EnglishLetter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ"
if InputUserWord in EnglishLetter and NumberOfCharacters == 1:
    print(InputUserWord.lower())
else:
    print("E2")



