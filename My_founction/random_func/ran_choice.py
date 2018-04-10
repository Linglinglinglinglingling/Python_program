import random
def random_choice(seq):
    n=len(seq)
    new_seq=[]
    ran_number=random.randint(0,n-1)
    max_loop_times=-1
    #use max_loop_time==a given number to stop at a random times,return the last item
    for i in seq:
        new_seq.append(i)
        max_loop_times+=1
        if max_loop_times==ran_number:
            return new_seq[-1]


if __name__ == '__main__':
    a={1,2,3,4}
    b=random_choice(a)
    print(b)