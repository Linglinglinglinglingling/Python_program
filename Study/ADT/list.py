# list.py: implementation of the List ADT using an array structure
class List:
    # creates a new list
    def __init__(self):
        self.the_list = []  # represent the list as a Python's list
        self.count = 0  # indicate the current size of the list

    # returns the number of items in the list
    def __len__(self):
        return self.count

    """
    # retrieve the item at a specific position 'index'
    def __getitem__(self, index):  # overload the index
        assert index >= 0 and index < len(self), "Index out of range"
        return self.the_list[index]

    # update the item at a specific position 'index' with a new value
    def __setitem__(self, index, value): # overload the =
        assert index >= 0 and index < len(self), "Index out of range"
        self.the_list[index] = value
        
    # Overload in
    def __contains__(self, item):
        if item in self.the_list:
            return True
        else:
            return False
            
    #Overload for loop,both iter and contain
    def __iter__
    """

    # returns True if the list is empty or False otherwise
    def is_empty(self):
        return len(self) == 0

    # adds a new item at the end of the list
    def add(self, item):
        # self.count indicates the next position to be added
        # at the end of the list
        self.the_list.append(item)
        self.count += 1

    # inserts a new item at a specific position 'index'
    # assuming the index is valid i.e. index >= 0 and index < len(self)
    def insert(self, index, item):
        # extend the list with one more item
        self.the_list.append(0)
        # shift all the items from index onwards one position
        # to the right to make room for the new item
        for i in range(len(self) - 1, index - 1, -1):
            self.the_list[i + 1] = self.the_list[i] #append 0 but count doesn't change,then shift to right and overwirte the 0
        self.the_list[index] = item
        self.count += 1

    # removes an existing item at a specific position 'index'
    # assuming the index is valid i.e. index >= 0 and index < len(self)
    def delete(self, index):
        assert not self.is_empty(), "Cannot remove from an empty list"
        # shift all the items after the item to be deleted
        # one position to the left
        for i in range(index, len(self) - 1):
            self.the_list[i] = self.the_list[i + 1] #left shift 1, delete item by use the right one to overwirte the item
        self.count -= 1
        del self.the_list[len(self)]

    # removes an existing item assuming the item is in the list
    def remove(self, item):
        assert not self.is_empty(), "Cannot remove from an empty list"
        # find the position of the item to be deleted
        for i in range(len(self)):
            if self.the_list[i] == item:
                index = i
                break
        # shift all the items after the item to be deleted
        # one position to the left
        for i in range(index, len(self) - 1):
            self.the_list[i] = self.the_list[i + 1]
        self.count -= 1
        del self.the_list[len(self)]

    # returns True if an item exists in the list or False otherwise
    def search(self, item):
        # check each item from the beginning of the list
        # to the end of the list
        for i in range(len(self)):
            if self.the_list[i] == item:
                return True
        return False

    # returns the position of an item if it exists in the list
    # or -1 if the item is not in the list
    def index(self, item):
        # check each item from the beginning of the list
        # to the end of the list
        for i in range(len(self)):
            if self.the_list[i] == item:
                return i
        return -1  # an invalid index (i.e. item does not exist)

    # returns a formatted string with the items in the list
    def __str__(self):
        output = ""
        for i in range(len(self)):
            output += (self.the_list[i] + " ")
        return output
