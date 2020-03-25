list_x = [4, 5, 6]
list_y = [1, 2, 3]


def extend_list_x(list_x, list_y):

    #list_x_y = [*list_y, *list_x]  # unpack both iterables in a list literal
    list_x_y = []
    list_x_y.append(list_x)
    list_x_y.append(list_y)
    return list_x_y


print(extend_list_x(list_x, list_y))