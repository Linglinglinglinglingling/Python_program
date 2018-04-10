# queue.py: implementation of the Queue ADT using an array structure
#           with unbounded capacity
class Queue:
    # creates a new queue
    def __init__(self):
        self.the_queue = []  # represent the queue as a list
        self.count = 0  # indicate the current size of the queue
        self.front = 0  # indicate the front of the queue
        self.rear = -1  # indicate the rear of the queue(i.e. the index of the last item)

    # returns the number of items in the queue
    def __len__(self):
        return self.count

    # returns True if the queue is empty or False otherwise
    def is_empty(self):
        return len(self) == 0

    # appends the given item at the end of the queue
    def append(self, item):
        self.the_queue.append(item)
        self.rear += 1
        self.count += 1

    # removes and returns the first item in the queue
    def serve(self):
        assert not self.is_empty(), "Cannot serve an empty queue"
        item = self.the_queue[self.front]
        self.front += 1
        self.count -= 1
        return item