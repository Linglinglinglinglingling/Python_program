# import the Queue class here
from Study.ADT.queue import Queue
def serve(arrive_time,serve_time):
    # define variables for arrival time and service time (you may change these later if you want)
    # create a new queue
        a = Queue()

        # define variables to keep track of the current time and service time (initialise them to 0)

        has_served_time = 0

        # other required variables
        customer_id = 1

        # this variable controls the access of a customer in the service area

        # it should be turned to True when the customer needs to be served; it remains False otherwise
        lock=False

        # simulation will run for 60 time units (you may change it later if you want)
        for i in range(1,121):
            # if the customer has not arrived... increment time unit by 1
            if i%arrive_time==0:  # <your check goes here># increment time based upon the variable# otherwise say that the customer with some unique ID has arrived
                print("The customer with id " + str(customer_id) + " has arrived"+'\t'+str(i))

                 # add customer to queue
                a.append(customer_id)
                # change the customer ID
                customer_id += 1
                # open the lock to the service area
                lock = True

            # if the customer has been served
            if lock==True:
                if has_served_time == serve_time:
                    b=a.serve()
                    if a.count==0:
                        has_served_time=0#
                    else:
                        has_served_time=1# in this minute, next customer is served
                                                # remove customer from queue and print which customer was served

                    print("The customer with id " + str(b) + " has been served"+'\t'+str(i))
                    # reset service time

                    # lock the area
                    if a.count==0:
                        lock=False
            # otherwise increment service time,
                else:
                    has_served_time+=1

    # increment time based upon the variable

serve(8,15)