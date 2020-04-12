

def print_hangman(num_of_tries):

    if num_of_tries < 8 and num_of_tries > 0:
        NUMBER_1 = "x-------x"
        NUMBER_2 = """x-------x\n|\n|\n|\n|\n|"""
        NUMBER_3 = """x-------x\n|       |\n|       0\n|\n|\n|"""
        NUMBER_4 = """x-------x\n|       |\n|       0\n|       |\n|\n|"""
        NUMBER_5 = """x-------x\n|       |\n|       0\n|      /|\\\n|\n|"""
        NUMBER_6 = """x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|"""
        NUMBER_7 = """x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"""
        HANGMAN_PHOTOS = {1: NUMBER_1, 2: NUMBER_2, 3: NUMBER_3, 4: NUMBER_4, 5: NUMBER_5,
                          6: NUMBER_6, 7: NUMBER_7}

        print(HANGMAN_PHOTOS[num_of_tries])
    else:
        print("please choose only number betwenn 1 to 7:")


def main():
    num_of_tries = 6
    print_hangman(num_of_tries)


if __name__ == "__main__":
    main()
