import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a_dataframe = pd.DataFrame(
               {'name':['Alice','Bob','Charles'],
                'age':[25, 23, 34],
                'gender':['female','male','male']})
print(a_dataframe)

# new_dataframe = pd.DataFrame(np.arange(16).reshape((4,4)),
#                 #x-axis and y -axis
#                 index = ['x1','x2','x3','x4'],
#                 columns = ['y1','y2','y3','y4'])
#
# #change previous x-axis:'x1','x2','x3','x4',  set new x axis start from 1 ,end at 4, 5-1=4
# new_dataframe.index = np.arange(1,5)
# print(new_dataframe)


new_dataframe[:4].plot()
plt.legend(loc="best")
plt.show()

new_dataframe[:4].plot(kind='bar', color=['magenta','yellow','cyan','lime'])

#legend change the lable location,best
	# upper right
	# upper left
	# lower left
	# lower right
	# right
	# center left
	# center right
	# lower center
	# upper center
	# center
plt.legend(loc="upper right")
plt.show()
