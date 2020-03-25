list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]

def are_lists_equal(list1, list2):
    sum_list1 = sum(list1)
    sum_list2 = sum(list2)
    if  sum_list1 == sum_list2 :
        return "true"
    else:
        return "false"

print (are_lists_equal(list1, list3))