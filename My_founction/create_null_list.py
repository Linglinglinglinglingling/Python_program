def create_empty_list(number):
    empty_list = []
    list = []
    for i in range(number):
        list.append(empty_list[:])
    return list

if __name__ == '__main__':
    a=create_empty_list(5)
    a[1]=10
    print(a)

