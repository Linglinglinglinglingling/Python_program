from ran_sample import random_sample
def random_shuffle(seq):

    n=len(seq)
    #the number of sample equals n, means shuffle the entire seq
    return random_sample(seq,n)



a={'a':'A','b':'B','c':'C'}
b=random_shuffle(a)
print(b)