import time
import random
import Study.Search_and_Sort.Bubble_sort
import Study.Search_and_Sort.Selection_sort
import Study.Search_and_Sort.merge_sort
import Study.Search_and_Sort.quick_sort
import string
import Study.Search_and_Sort.Insertion_sort
import numpy as np
import matplotlib.pyplot as plt

ranlist=[]
# for i in range(500):
#     a=random.randint(1,1000)
#     ranlist.append(a)
#     b=ranlist[:]
#     start_time=time.clock()
#     Insertion_sort.insertion_sort(b)
#     #Bubble_sort.bubble_sort(b)
#     #Selection_sort.selection_sort(b)
#     end_time=time.clock()
#     run=(end_time-start_time)*100000
#     runtime.append(run)
#
# average = sum(runtime) / len(runtime)
# print('{0:.3f}'.format(average))



#for reverse order,fixed list size 100 run 500 times

#run three times, first--bubble, second--selection,last time--insertion
list_all_runtime=[]
for j in range(5):
    runtime = []
    for i in range(1,501):
        #create a list in reversed order  [100,99,98...1]
        #ranlist=list(range(100,0,-1))
        ranlist=[random.randint(0,200) for k in range(100)]
        b=ranlist[:]

        start_time = time.clock()
        if j==0:
            Study.Search_and_Sort.Bubble_sort.bubble_sort(b)
        elif j==1:
            Study.Search_and_Sort.Selection_sort.selection_sort(b)
        elif j==2:
            Study.Search_and_Sort.Insertion_sort.insertion_sort(b)
        elif j==3:
            Study.Search_and_Sort.quick_sort.quick_sort(b)
        else:
            Study.Search_and_Sort.merge_sort.merge_sort(b)
        end_time = time.clock()
        run = (end_time - start_time)
        runtime.append(run)
        #append the list of runtime as one time into a list
        if i==500:
            list_all_runtime.append(runtime)

x_axis=np.arange(1.,501.)
#first--bubble,second--selection,third--insertion, fourth--quick_sort, fifth--merge_sort
plt.plot(x_axis,list_all_runtime[0],'r',x_axis,list_all_runtime[1],'b',x_axis,list_all_runtime[2],'g',
         x_axis,list_all_runtime[3],'y',x_axis,list_all_runtime[4],'m')
plt.show()


