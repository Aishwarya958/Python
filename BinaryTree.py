class BinaryTree(object):
  ''' Represents a binary tree '''
  
  class Node(object):
    ''' Represents a node in the binary tree '''
     
    
    def __init__(self, data):
      ''' Constructor for Node '''
      self.data = data
      self.left = None
      self.right = None  
  
  def __init__(self):
    ''' Constructor for Binary Tree '''
    self.root = None  
      
  def insert(self, data):
    ''' Inserts nodes in Binary Tree '''
    insert_node = self.Node(data)
    if self.root is None:
	self.root = insert_node
        return "Inserted at root"

    else :
      current = self.root	
      while True:
        if data < current.data:
	  if current.left is None:
	    current.left = insert_node
            return "Inserted at left"
            break
	  current = current.left	

	if data > current.data:
	  if current.right is None:    
	    current.right = insert_node
            return "Inserted at left"
	    break	  
	  current = current.right

        else:
          return "Already Exists"
        
  
  def find(self, data):
    ''' Finds a  node in Binary Tree '''
    current = self.root
    if data == current.data:
     return "Found the element '{}'".format(data)
   
    while current is not None:
     if data == current.data:
       return "Found the element '{}'".format(current.data)
     elif data < current.data:
       current = current.left 
     else:
       current = current.right     
    return "Found the element '{}'".format(current.data)
   
  
  
  def level_order(self):
    ''' Prints the Binary Tree in Breadth First Search Format '''
    queue = [self.root]
    levellist = []
    while queue:
      current = queue.pop(0)
      levellist.append(current.data)
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
    return levellist
  
  def inorder(self):
    ''' Prints the Binary Tree in Inorder'''
    stack = []
    p = []
    current = self.root
    
    while stack  or current :
      if current :
        stack.append(current)
        current = current.left
      else:
       current = stack.pop()
       p.append(current.data)
       current = current.right
    return p
   
     
  def preorder(self):
    ''' Prints the Binary Tree in Preorder'''
    stack = [self.root]
    p = []
    while stack :
      current = stack.pop()
      p.append(current.data)
      if current.right:
        stack.append(current.right)
      if current.left :
        stack.append(current.left)  
    return p        
      
  def postorder(self): 
    ''' Prints the Binary Tree in Postorder'''
    stack = []
    printstack = []  
    p = []   
  
    stack.append(self.root)   
    while stack:      
        current = stack.pop()
        printstack.append(current)     
       
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None :
            stack.append(current.right)
       
    while(printstack):
        current = printstack.pop()
        p.append(current.data)
    return p
    
if __name__ == '__main__':

    tree = BinaryTree()
    tree.insert(10)
    tree.insert(2)
    tree.insert(11)
    tree.insert(6)
    tree.insert(23)
    
    
  
  
