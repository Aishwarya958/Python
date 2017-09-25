#Implementation of stack using List in python

class Stack(object):
  ''' Represents a stack i.e. FILO '''
  def __init__(self):
    self._stack = []
  
  def push(self, data):
    '''  Pushes the data on the top of the stack '''
    self._stack.append(data)   
    
  
  def pop(self):
    ''' Removes  the data on the top of the stack '''
    return self._stack.pop()
  
  @property
  def top(self):
    ''' Should return the data at the top of the stack without removing it'''
    return self._stack[0]

  @property
  def get_stack(self):
    return self._stack

if __name__ == '__main__':

    stackobj = Stack()
    stackobj.push(10)
    stackobj.push(20)
   

    print("\nThe top elemet  is {}".format(stackobj.top))
    stackobj.pop()
   
    
    
    
  
  
