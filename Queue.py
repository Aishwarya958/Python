# In the following assignment, you will be implementing three separate classes.
#
# 1. Queue
# 2. Stack
# 3. Binary Tree
#
# Do not use any module/libraries and implement these classes using simple Python
# data structures.
# 
# You are also expected to write some unit tests for your implementation.
# Please use the Python unittest module for writing your unit tests and generate a code
# coverage report as well.

class Queue(object):
  ''' Represents a queue i.e. FIFO '''
  def __init__(self):    
      self._queue = [] 
  
  def enqueue(self, data):
    ''' Adds the data at the end of the queue using the append function'''
    self._queue.append(data)     

  
  def dequeue(self):
    ''' Removes the data from the front of the queue using pop(0) and return it '''
    return self._queue.pop(0)
  
  @property
  def front(self):
    ''' Prints the data at the front of the list '''
    front = self._queue[0]
    return front


    
if __name__ == '__main__':

    queue_obj = Queue()
    queue_obj.enqueue(10)
    queue_obj.enqueue(20)
    
    
  
  
