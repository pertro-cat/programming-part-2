import unittest
from src.avl_priority_queue import AVLPriorityQueue

class TestAVLPriorityQueueInsert(unittest.TestCase):
    def setUp(self):
        self.queue = AVLPriorityQueue()

    def test_insert_single_item(self):
        self.queue.insert(10, 1)
        self.assertEqual(self.queue.traverse(self.queue.root), [10], "Insertion of a single item should work")

    def test_insert_multiple_items(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.queue.insert(30, 3)
        self.assertEqual(sorted(self.queue.traverse(self.queue.root)), sorted([10, 20, 30]),
                         "Insertion of multiple items should work")

    def test_insert_duplicate_priority(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.queue.insert(30, 3)
        self.queue.insert(40, 3)
        self.assertEqual(sorted(self.queue.traverse(self.queue.root)), sorted([10, 20, 30, 40]),
                         "Insertion of items with duplicate priorities should work")

    def test_no_duplicates(self):
        self.queue.insert(10, 1)
        self.queue.insert(20, 2)
        self.queue.insert(30, 3)
        self.queue.insert(40, 4)
        self.queue.insert(50, 5)
        self.queue.insert(60, 6)
        self.queue.insert(70, 7)

if __name__ == '__main__':
    unittest.main()
