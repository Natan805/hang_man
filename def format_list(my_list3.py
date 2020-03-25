my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium", "y", "and", "X", "ASD"]


def format_list(my_list):
    """The function accepts a string of double-length strings.  The function returns a string containing the list
    organs in the spousal positions, separated by commas and spaces,
    as well as the last limb with the caption "and" before it.
    :type: list
    :return:  give the pair result with comma and last limb with the caption "and"
    :rtype: str"""

    # Getting Pair word from the list
    pair = my_list[slice(0, -1, 2)]

    # Getting the Pair variable without the end word
    pair_len_minus_one = len(pair) - 1
    pair_without_end_word = pair[0:pair_len_minus_one]

    # Getting only the end word
    end_pair_words = [pair[-1]]

    # Convert to str, separated by commas and spaces, as well as the last limb with the caption "and" before it
    x = ", ".join(pair_without_end_word)
    y = "".join(end_pair_words)
    plus_and = " and "

    return x + plus_and + y


print(format_list(my_list))
