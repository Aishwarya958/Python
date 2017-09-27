# Implementation of Queue using List in Python


class Queue(object):
    ''' Represents a queue i.e. FIFO '''
    def __init__(self):
        self._queue = []

    def enqueue(self, data):
        ''' Adds the data at the end of the queue using the append function'''
        self._queue.append(data)

    def dequeue(self):
        ''' Removes the data from the front
         of the queue using pop(0) and return it '''
        return self._queue.pop(0)

    @property
    def front(self):
        ''' Prints the data at the front of the list without popping it '''
        front = self._queue[0]
        return front

    def print_queue(self):
        ''' Prints the current data in the queue'''
        print "Elements in the queue are : "
        for x in self._queue:
            print x,

    @property
    def get_queue(self):
        return self._queue

if __name__ == '__main__':

    queueobj = Queue()
    queueobj.enqueue(10)
    queueobj.enqueue(20)

    print("The front element is {}".format(queueobj.front))

    queueobj.dequeue()
    queueobj.print_queue()
