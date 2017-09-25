import unittest
from binarytree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    
  def setUp(self):
    self.tree = BinaryTree()
    self.tree.insert(10)
    self.tree.insert(2)
    self.tree.insert(11)
    self.tree.insert(6)
    self.tree.insert(23)

  def test_insert(self):
   tree1 = BinaryTree()
   self.assertEqual(tree1.insert(25),"Inserted at root")
   self.assertEqual(tree1.insert(25),"Already Exists")
   self.assertEqual(tree1.insert(10),"Inserted at left")
   self.assertEqual(tree1.insert(30),"Inserted at right")

  def test_level_order(self):
   self.assertEqual(self.tree.level_order(),[10, 2, 11, 6, 23])
   
  def test_inorder(self):
   self.assertEqual(self.tree.inorder(),[2, 6, 10, 11, 23])

  def test_preorder(self):
   self.assertEqual(self.tree.preorder(),[10, 2, 6, 11, 23])

  def test_postorder(self):
   self.assertEqual(self.tree.postorder(),[6, 2, 23, 11, 10])

  def test_find(self):
   self.assertEqual(self.tree.find(6),"Element '6' Found in the Tree")
   self.assertEqual(self.tree.find(10),"Element '10' Found in the Tree")
   self.assertEqual(self.tree.find(43),"Element '43' not Found in the Tree")


 

if __name__ == '__main__':
  unittest.main()
  
 
