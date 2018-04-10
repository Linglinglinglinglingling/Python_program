import random
#alter the random_choice to get both the item and random number that generate the item
def random_choice_newreturn(seq):
    n=len(seq)
    new_seq=[]
    ran_number=random.randint(0,n-1)
    max_loop_times=-1
    #stop at a random times,return the last item
    for i in seq:
        new_seq.append(i)
        max_loop_times+=1
        if max_loop_times==ran_number:
            return (new_seq[-1],ran_number)

def random_sample(seq,k):
    #max index
    n=len(seq)-1
    list_sample=[]
    list_ran_number=[]
    i=0
    #each time get a random item from seq, run k times
    while i<k:
        while True:
            ran_item=random_choice_newreturn(seq)
            #check the random number is already chosen or not
            #if not,break the loop and append item into item_list
            #append random number in random_number list
            if not(ran_item[1] in list_ran_number):
                break
        list_sample.append(ran_item[0])
        list_ran_number.append(ran_item[1])
        i+=1
    return list_sample

if __name__ == '__main__':

    a={1,2,3,4}

    b=random_sample(a,3)
    print(b)




