import time
def sum_f(a,**kwargs):
    for i in kwargs:
        print(a,i,kwargs[i])
time.clock()
c=sum_f
print(c)