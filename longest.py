
list1 = ["111", "234", "2000", "goru", "birthday", "09"]


def longest(my_list):
    list1.sort(key=len)
    return (list1[-1])

print (longest(list1))