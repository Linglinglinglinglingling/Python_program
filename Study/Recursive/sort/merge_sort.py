def merge_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    if n > 1:  # check for base case---each list has only 1 item
        # find the middle of the list
        mid = n // 2

        # based upon the middle index, two sublists are then created
        # from the 0 index until the mid-1 index
        left_sublist = the_list[:mid]
        # from the mid index until the n - 1 index
        right_sublist = the_list[mid:]
        print("Splitting: " + str(left_sublist) + " and " + str(right_sublist))

        # merge sort is called again on the two new created sublists
        merge_sort(left_sublist)
        merge_sort(right_sublist)

        # sort and merge
        print("Merging " + str(left_sublist) + " with " + str(right_sublist))
        i = 0  # index for left sublist
        j = 0  # index for right sublist
        k = 0  # index for main list


        #merge the left and right list to the result list( just replace the item
        # in the original list)

        #compare two list, add the smaller item into result list, then smaller list
        #index +1(pointer) , and result list's index +1(pointer)
        while i < len(left_sublist) and j < len(right_sublist):
            if left_sublist[i] <= right_sublist[j]:
                the_list[k] = left_sublist[i]
                i += 1
            else:
                the_list[k] = right_sublist[j]
                j += 1
            k += 1


        #insert the remaining elements into main list,because we just replace the original
        #list's item, we didn't append the item into a new list, so we can't use the extend
        #function
        while i < len(left_sublist):
            the_list[k] = left_sublist[i]
            i += 1
            k += 1

        while j < len(right_sublist):
            the_list[k] = right_sublist[j]
            j += 1
            k += 1


        print("After merging the list is: " + str(the_list))

if __name__ == '__main__':

    a=[4,3,2,1]
    merge_sort(a)