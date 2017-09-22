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
class Stack(object):
  ''' Represents a stack i.e. FILO '''
  def __init__(self):
    self._stack = []
  
  def push(self, data):
    ''' Should push the data on the top of the stack '''
    self._stack.insert(0,data)   
    
  
  def pop(self):
    return self._stack.pop(0)
  
  @property
  def top(self):
    ''' Should return the data at the top of the stack '''
    return self._stack[0]


if __name__ == '__main__':

    stack_obj = Stack()
    stack_obj.push(10)
    stack_obj.push(20)

    
    
  
  
