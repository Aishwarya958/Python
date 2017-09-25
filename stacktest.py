import unittest
from stack import Stack

class TestStack(unittest.TestCase):
  def setUp(self):
    self.obj = Stack()	
	
  def test_push(self):
				
    self.obj.push(10)
    self.assertEqual(self.obj._stack,[10])

    self.obj.push(20)
    self.assertEqual(self.obj._stack,[20,10])

	

  def test_pop(self):
		
    self.obj.push(10)	
    self.obj.push(20)		
    result = self.obj.pop()		
    self.assertEqual(str(result),"20")
	
    result1 = self.obj.pop()
    self.assertEqual(str(result1),"10")

  def test_top(self) :

    self.obj.push(10)	
    self.obj.push(20)	
    result = self.obj.top
    self.assertEqual(str(result),"20")

if __name__ == '__main__':
  unittest.main()
