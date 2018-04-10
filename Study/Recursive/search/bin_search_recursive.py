def recursive_binary_search(the_list, target_item):
    # repeatedly divide the list into two halves
    # as long as the target item is not found

    if len(the_list) == 0:  # the list cannot be divided further
        return False
    else:
        # find the middle position
        mid = len(the_list) // 2

        # check if the target is equal to the middle item
        if the_list[mid] == target_item:
            return True

        # check if the target is less than the middle item
        # lower half to be considered
        elif target_item < the_list[mid]:
            # create a smaller list,used to divide the list
            smaller_list = the_list[:mid]
            # call the function itself with the lower half
            return recursive_binary_search(smaller_list, target_item)

        # the target is greater than the middle item
        # upper half to be considered
        else:
            # create a smaller list
            smaller_list = the_list[mid + 1:]
            # call the function itself with the upper half
            return recursive_binary_search(smaller_list, target_item)

if __name__ == '__main__':
    a=[1,2,3,4,5]
    b=recursive_binary_search(a,7)
    print(b)