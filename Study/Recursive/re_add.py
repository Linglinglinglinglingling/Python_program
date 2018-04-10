def add(a,b):
    if a==0:
        if b==0:
            return 0
        else:
            return add(a,b-1)+1
    else:
        if b==0:
            return add(a-1,b)+1
        else:
            return add(a-1,b-1)+1+1


a=add(19,9)
print(a)