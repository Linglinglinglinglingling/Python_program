def binary_search(the_list, target_item):
    # indicate the start and the end of the list to be considered
    low = 0
    high = len(the_list) - 1

    # repeatedly divide the list into two halves
    # as long as the target item is not found
    while low <= high:

        # find the middle position
        mid = (low + high) // 2

        # check if the target is equal to the middle item
        if the_list[mid] == target_item:
            return True
        # check if the target is less than the middle item
        elif target_item < the_list[mid]:
            high = mid-1 # lower half to be considered
        # the target is greater than the middle item
        else:
            low = mid + 1  # upper half to be considered

    # the list cannot be divided further and the target is not found
    return False