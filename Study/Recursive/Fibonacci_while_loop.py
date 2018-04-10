def f(n):
    #start from 1,2
    if n==2:
        return 2
    i=3
    #first item in calculation
    f_item=1
    s_item=1
    while i<=n:
        a=f_item+s_item
        #1(f_item)+2(s_item) becomes   2(f_item)+3(s_item)
        s_item,f_item=a,s_item
        i+=1
    return a

if __name__ == '__main__':
    a=f(50)
    print(a)