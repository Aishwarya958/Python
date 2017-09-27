# Implementation of Binary Tree In Python
from stack import Stack
from queue import Queue


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
        # If there is no node insert the node at the root
        if self.root is None:
            self.root = insert_node
            return "Inserted at root"
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = insert_node
                        return "Inserted at left"
                        break
                    current = current.left

                if data > current.data:
                    # If the node is greater than its root node insert at right
                    if current.right is None:
                        current.right = insert_node
                        return "Inserted at right"
                        break
                    current = current.right

                else:				# If the node is already present in the tree
                    return "Already Exists"

    def find(self, data):
        queue = Queue()
        queue.enqueue(self.root)

        while queue.get_queue:
            current = queue.front
            if(current.data == data):	      		# If the queue has the element
                return "Element '{}' Found in the Tree".format(current.data)
            queue.dequeue()		      		 # Remove element is found
            if current.left is not None:
                queue.enqueue(current.left)   		# Search at the left Tree
            if current.right is not None:
                queue.enqueue(current.right)  		# Search at the right Tree
        return "Element '{}' not Found in the Tree".format(data)

    def level_order(self):
        ''' Prints the Binary Tree in Breadth First Search Format '''
        queue = Queue()
        queue.enqueue(self.root)
        levellist = []		# To print the BFS result
        while queue.get_queue:
            current = queue.dequeue()
            levellist.append(current.data)
            if current.left:
                queue.enqueue(current.left)    # Append the left Tree
            if current.right:
                queue.enqueue(current.right)    # Append the right Tree
        return levellist

    def inorder(self):
        ''' Prints the Binary Tree in Inorder'''
        stack = Stack()
        p = []
        current = self.root

        while stack.get_stack or current:
            if current:
                stack.push(current)
                current = current.left		# The Left side of current Root
            else:
                current = stack.pop()
                p.append(current.data)		# The current Root
                current = current.right		# The Right side of current Root
        return p

    def preorder(self):
        ''' Prints the Binary Tree in Preorder'''
        stack = Stack()
        stack.push(self.root)
        p = []
        while stack.get_stack:
            current = stack.pop()
            p.append(current.data)		# The current Root
            if current.right:
                stack.push(current.right)    # The Left side of current Root
            if current.left:
                stack.push(current.left)  	# The Left side of current Root
        return p

    def postorder(self):
        ''' Prints the Binary Tree in Postorder'''
        stack = Stack()
        printstack = Stack()
        p = []

        stack.push(self.root)
        while stack.get_stack:
            current = stack.pop()
            printstack.push(current)
            if current.left is not None:
                stack.push(current.left)
            if current.right is not None:
                stack.push(current.right)

        while(printstack.get_stack):
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

    print tree.find(23)
    print "Level order is :", tree.level_order()
    print "Pre order is :", tree.preorder()
    print "In order is :", tree.inorder()
    print "Post order is :", tree.postorder()
