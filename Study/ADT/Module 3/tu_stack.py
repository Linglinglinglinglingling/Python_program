# Given size stack
class Tu_stack:
    # creates a new stack
    def __init__(self,size):
        a=[0]*size
        self.the_stack =a[:]  # represent the stack as a list
        self.top = -1  # indicate the top position of the stack
        self.size=size



    # returns True if the stack is empty or False otherwise
    def is_full(self):
        return self.top>(self.size-1)

    # pushes an item onto the top of the stack
    def push(self, item):
        self.top += 1
        assert not self.is_full(),"can't push, the stack is full"
        self.the_stack[self.top]=item


    # removes and returns the top item on the stack
    def pop(self):
        item = self.the_stack[self.top]
        del self.the_stack[len(self.the_stack)]
        self.top -= 1
        return item

    # returns the item on the stack without removing it
    def peek(self):
       item = self.the_stack[self.top]
       return print(item)

a=Tu_stack(5)