import numpy as np
import matplotlib.pyplot as plt

#zhuan zhi
a=np.array([[1,2,3],[4,5,6]]).T
print(a)


a=np.arange(12).reshape(4,3)
print(a)

#0-9
b=np.arange(10)
print(b)

#all item are zero
zero_array = np.zeros((2,3))
print(zero_array)

#all items are one
one_array = np.ones((3,3))
print(one_array)