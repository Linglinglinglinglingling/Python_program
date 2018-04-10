# sorts the list in an ascending order using selection sort
def selection_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    # perform n-1 iterations on the entire list
    for i in range(n - 1):
        # assume the item at index i is the smallest
        smallest = i
        # check if any other item is smaller than the current smallest
        for j in range(i + 1, n):
            if the_list[j] < the_list[smallest]:
                smallest = j  # update the current j as the smallest

        tmp=the_list[i]
        the_list[i]=the_list[smallest]
        the_list[smallest]=tmp
    return the_list