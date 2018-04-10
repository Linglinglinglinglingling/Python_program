#input a number of object, how many combination can have
#e.g. 3 ----123,132,213,231,312,321, return 6
from math import *

num_of_objects = int(input("Please input the number of unique objects: "))

print("There are " + str(factorial(num_of_objects)) + " of arrangements.")