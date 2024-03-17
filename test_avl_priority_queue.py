import unittest
import sys
sys.path.append('C:\\Python\\PycharmProjects\\programming_part2\\lab3')
from src.avl_priority_queue import AVLPriorityQueue


from avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = AVLPriorityQueue()

    def test_insert(self):
        self.queue.insert(10, 1)
        self.assertEqual(self.queue.peek(), 10)

    def test_remove(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.assertEqual(self.queue.remove(), 20)

    def test_peek(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.assertEqual(self.queue.peek(), 20)

    def test_traverse(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.assertEqual(self.queue.traverse(self.queue.root), [20, 10])

if __name__ == '__main__':
    unittest.main()