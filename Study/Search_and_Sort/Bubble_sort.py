# sorts the list in an ascending order using Bubble sort

def bubble_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    # perform n-1 iterations on the entire list
    for i in range(n - 1, 0, -1):
        # for each iteration, move the largest item to the end
        for j in range(i):
            if the_list[j] > the_list[j + 1]:
                # swap if two adjacent items are out of order
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp
    return the_list



# sorts the list in an ascending order using Bubble sort
def my_bubble_sort(the_list):
    # obtain the length of the list
    n = len(the_list)

    # perform n-1 iterations on the entire list
    for i in range(n - 1):
        # for each iteration, move the largest item to the end
        for j in range(n-1-i):
            if the_list[j] > the_list[j + 1]:
                # swap if two adjacent items are out of order
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp
    return the_list

def my_bubble_sort_reverse(the_list):
    # obtain the length of the list
    n = len(the_list)

    # perform n-1 iterations on the entire list
    for i in range(n - 1):
        # for each iteration, move the largest item to the end
        for j in range(n-1,i,-1):
            if the_list[j] > the_list[j - 1]:
                # swap if two adjacent items are out of order
                the_list[j],the_list[j-1]=the_list[j-1],the_list[j]
    return the_list

if __name__ == '__main__':
    a=[1,2,3,4,5]
    b=my_bubble_sort_reverse(a)
    print(b)