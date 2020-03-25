def shift_left(a, b, c):
    """This function get 3 list and move it left
    :param a: list 1
    :param b: list 2
    :param c: list 3
    :type list
    :return  give rsult A and replace with B and B replace with C so C replace with A
    :rtype list"""
    #This get the paramter A and replace with B and B replace with C so C replace with A
    x = a
    a = b
    b = c
    c = x
    return (a, b, c)

print (shift_left("a", 2, 3))
