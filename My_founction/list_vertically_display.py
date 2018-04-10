a=[1,2,3]
b=[4,5,6,7,8]
c=[9,10,100]
d=[a,b,c]
#print(d)
new_list=[]

for index,list in enumerate(d):
    for list_index,item in enumerate(list):
        #if the sub_list inside d is longer then new list(each item in sublist need to append
        #to the first location of a new list) ---then new list won't have enough sub
        #list for the item to append to
        while len(d[index])>len(new_list):
            new_list.append([])

        #for the first time, put item into the first location of each list,
        #then second time ,put item into the second location of each list,
        #in case the list don't have the second location, append ' ' as place holde
        #later ,replaced by the item

        while  index>len(new_list[list_index])-1:
            new_list[list_index].append(' ')
            #list_index +1 each loop, index stay same ---so append the item to first location
            #of all the list(i.e vertically displayed)

        new_list[list_index][index]=item

print(new_list)