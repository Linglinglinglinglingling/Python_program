import threading
import time

exitFlag = 0

# create a subclass of Thread class
class myThread (threading.Thread):

    #override __inti__ to add additional arguments
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

    #override run() to implement what tread do
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2) #last argument is the delay in time.sleep() in print_time func

# Start new Threads
thread1.start()
thread2.start()

thread_list=[]
thread_list.append(thread1)
thread_list.append(thread2)
for thread in thread_list:
    thread.join()
print("Exiting Main Thread")
