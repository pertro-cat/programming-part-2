import unittest

from src.find_successor import find_successor, BinaryTree

class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
        self.node1 = BinaryTree(1)
        self.node3 = BinaryTree(3)
        self.node2 = BinaryTree(2, left=self.node1, right=self.node3)
        self.node1.parent = self.node2
        self.node3.parent = self.node2

        self.node5 = BinaryTree(5)
        self.node7 = BinaryTree(7)
        self.node6 = BinaryTree(6, left=self.node5, right=self.node7)
        self.node5.parent = self.node6
        self.node7.parent = self.node6

        self.node4 = BinaryTree(4, left=self.node2, right=self.node6)
        self.node2.parent = self.node4
        self.node6.parent = self.node4

    def test_find_successor(self):
        self.assertEqual(find_successor(self.node1), self.node2, "Should be 2")
        self.assertEqual(find_successor(self.node2), self.node3, "Should be 3")
        self.assertEqual(find_successor(self.node3), self.node4, "Should be 4")
        self.assertEqual(find_successor(self.node4), self.node5, "Should be 5")
        self.assertEqual(find_successor(self.node5), self.node6, "Should be 6")
        self.assertEqual(find_successor(self.node6), self.node7, "Should be 7")
        self.assertEqual(find_successor(self.node7), None, "Should be None")

if __name__ == '__main__':
    unittest.main()
