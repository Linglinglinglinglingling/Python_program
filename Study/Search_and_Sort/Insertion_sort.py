# sorts the list in an ascending order using insertion sort
def insertion_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    # begin with the first item of the list
    # treat it as the only item in the sorted sublist
    for i in range(1, n):
        # indicate the current item to be positioned
        current_item = the_list[i]

        # find the correct position where the current item
        # should be placed in the sorted sublist
        pos = i
        while pos > 0 and the_list[pos - 1] > current_item:
            # shift items in the sorted sublist that are
            # larger than the current item to the right
            the_list[pos] = the_list[pos - 1]
            pos -= 1

        # place the current item at its correct position
        the_list[pos] = current_item
    return the_list