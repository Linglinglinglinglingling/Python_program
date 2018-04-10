# swap two item in a given list
def swap(list,index1,index2):
    assert index1<len(list) and index2< len(list), 'index out of range'
    a=list[index1]
    list[index1]=list[index2]
    list[index2]=a
    return None

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7]
    swap(a,-1,6)
    print(a)