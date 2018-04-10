# import the Queue class here
from Study.ADT.queue import Queue

# define variables for arrival time and service time (you may change these later if you want)
customer_arrival_time = 10
customer_service_time = 20

# create a new queue
a = Queue()

# define variables to keep track of the current time and service time (initialise them to 0)
cur_time = 0
ser_time = 0

# other required variables
customer_id = 1

# this variable controls the access of a customer in the service area

# it should be turned to True when the customer needs to be served; it remains False otherwise
lock=False

# simulation will run for 60 time units (you may change it later if you want)
for i in range(1,121):
    # if the customer has not arrived... increment time unit by 1
    if i%10==0:  # <your check goes here># increment time based upon the variable# otherwise say that the customer with some unique ID has arrived
        print("The customer with id " + str(customer_id) + " has arrived     "+str(i))
        # reset the time counter


        # add customer to queue
        a.append(customer_id)
        # change the customer ID
        customer_id += 1
        # open the lock to the service area
        lock = True

    # if the customer has been served
    if lock==True and ser_time==20:
        b=a.serve()
        ser_time=1
                                    # <your check goes here>
                                    # remove customer from queue and print which customer was served

        print("The customer with id " + str(b) + " has been served    "+str(i))
        # reset service time

        # lock the area
        if a.count==0:
            lock=False
    # otherwise increment service time
    elif lock==True :
        ser_time+=1

# increment time based upon the variable
