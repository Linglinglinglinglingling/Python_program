def quick_sort(the_list):
    # pass the indices of first and last elements of the list
    first = 0
    last = len(the_list) - 1
    quick_sort_aux(the_list, first, last)


def quick_sort_aux(the_list, first, last):
    # if it is not the base case
    if first < last:
        # find the partition point
        partition_point = partitioning(the_list, first, last)

        print("partition at index: ", partition_point)
        print(the_list)
        print("after partitioning: " + str(the_list[first:partition_point]) + \
              " and " + str(the_list[partition_point + 1:last + 1]))

        # call the quick sort function again on the new sublists
        quick_sort_aux(the_list, first, partition_point - 1)
        quick_sort_aux(the_list, partition_point + 1, last)


def partitioning(the_list, first, last):
    # take first element of the list is the pivot
    pivot_value = the_list[first]
    print("pivot: ", pivot_value)

    # these two indices will help us in locating the index point where the list will be partitioned
    left_index = first + 1
    right_index = last

    complete = False

    while not complete:
        # start with the left index and keep on incrementing it
        # until a value greater than the pivot value is found
        while left_index <= right_index and \
                        the_list[left_index] <= pivot_value:
            left_index += 1

        # now look for element from the right of the list
        # which is smaller than the pivot value
        while right_index >= left_index and \
                        the_list[right_index] >= pivot_value:
            right_index -= 1

        # check whether left and right indices have crossed each other
        # if that is the case exit the while loop
        if right_index < left_index:
            complete = True
        else:
            # otherwise swap the two elements
            the_list[left_index], the_list[right_index] \
                = the_list[right_index], the_list[left_index]

    # swap the pivot element with the element of the right index
    the_list[first], the_list[right_index] \
        = the_list[right_index], the_list[first]

    # return right index which is the partition point
    return right_index


if __name__ == '__main__':
    a=[2,3,4,1]
    quick_sort(a)

    print(a)