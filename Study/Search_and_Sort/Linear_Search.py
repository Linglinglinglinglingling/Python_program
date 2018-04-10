def linear_search(the_list, target_item):
    # obtain the length of the_list
    n = len(the_list)

    for i in range(n):
        # if the target is found
        if the_list[i] == target_item:
            return True

    # search through the list and the target is not found
    return False

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
       if v == target:
           return i
    return False