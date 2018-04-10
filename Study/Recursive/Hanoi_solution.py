import time

#solution to any height hanoi: move all item except the bottom item from orginal peg
#to the transitive peg, then move the left which is the largest one to the correct peg,
# then move the transitive peg to the correct peg



#logic: a function to move the pieces to the right location

#base case: height ==1, then move the piece to the right spot

#convergence: devide all item into two parts--bottom one and the rest. we need to move
#the rest part to the correct location,in this case, middle spot. then move the bottom to the
#right spot and move the rest to the right spot. But we don't now how the move the rest
#part to the middle spot, so we divide the rest part again to two parts--bottom one and rest part
#in this time, the destination locaton becomes to middle spot. So we need to move the rest
#part to the correct location,in this case ,right spot, then move the bottomo to the middle sport
#and move the rest part to the middle spot
# do this step recursively until reach the height==1
def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        #t1=time.clock()
                                #left peg   middle   right
        move_tower(height - 1, from_pole, with_pole, to_pole)
        #move_disk(from_pole, to_pole)
        print(from_pole,'to',to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)
        #t2=time.clock()
        #t=(t2-t1)*10000
       # print(t,height)


def move_disk(from_pole, to_pole):
    pass
    #print("moving disk from", from_pole, "to", to_pole)
    #list.append([from_pole,to_pole])

# three disks with three pegs (A, B, and C)

#increase as 2 to the power of n

#need to remove the def function
def num_call():
    for i in range(1,11):
        list=[]
        move_tower(i, "A", "C", "B")
        print(len(list))

def func_time():
    t3=time.clock()
    move_tower(3,'A','C','B')
    t4=time.clock()
    print((t4-t3)*10000)

move_tower(3,'A','C','B')

#no