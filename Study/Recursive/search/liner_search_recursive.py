#check the last item each time, then decrease the list size by 1( ie. drop the last item)
def liner_recursive(list,item):
    n=len(list)-1
    if n<0:
        return False
    elif list[n]==item:
        return True
    else:
        return liner_recursive(list[:n],item)
        #if need to check from the first item, then return line_recursive(list[1:],item)

if __name__ == '__main__':

    a=[1,2,3,4,5]
    b=liner_recursive(a,0)
    print(b)