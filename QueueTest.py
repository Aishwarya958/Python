import unittest
import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
      self.obj = Queue()	
	
    def test_enqueue(self):
				
      self.obj.enqueue(10)
      self.assertEqual(self.obj._queue,[10])

      self.obj.enqueue(20)
      self.assertEqual(self.obj._queue,[10,20])

	

    def test_dequeue(self):
		
      self.obj.enqueue(10)	
      self.obj.enqueue(20)		
      result = self.obj.dequeue()		
      self.assertEqual(str(result),"10")
	
      result1 = self.obj.dequeue()
      self.assertEqual(str(result1),"20")

    def test_front(self) :

      self.obj.enqueue(10)	
      self.obj.enqueue(20)	
      result = self.obj.front
      self.assertEqual(str(result),"10")

if __name__ == '__main__':
	unittest.main()
