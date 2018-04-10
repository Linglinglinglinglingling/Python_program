def sub_list_sum(list):
    total=0
    for i in list:
        if isinstance(i,int):# can be written as type(i)==type(1)
            total+=i
        else:
            total+=sub_list_sum(i)
    return total


if __name__ == '__main__':
    a=[1,2,3,[3,5],6]
    b=sub_list_sum(a)
    print(b)
