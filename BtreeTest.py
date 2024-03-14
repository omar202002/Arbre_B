import unittest
from Btree import *
from Node import *

class TestBtree(unittest.TestCase):

    def setUp(self):
        self.btree = Btree(3)
        
        self.node1 = Node(3 ,True)
        self.node2 = Node(3 ,False)
        self.node3 = Node(3 ,True)

        self.btree.root = self.node2

        self.node1.keys = [2]
        self.node2.keys = [3]
        self.node3.keys = [4,5]

        self.node2.children = [self.node1, self.node3]
        self.btree.nodes = [self.node2, self.node3, self.node1]

        self.node1.parent = self.node2
        self.node3.parent = self.node2

        self.btree.root = self.node2

    def test_search_key(self):
        self.assertTrue(self.btree.search_key(self.btree.root, 2))
        self.assertTrue(self.btree.search_key(self.btree.root, 3))
        self.assertTrue(self.btree.search_key(self.btree.root, 4))
        self.assertTrue(self.btree.search_key(self.btree.root, 5))

        self.assertFalse(self.btree.search_key(self.node1, 3))
        self.assertTrue(self.btree.search_key(self.node1, 2))

        self.assertFalse(self.btree.search_key(self.btree.root, 1))
        self.assertFalse(self.btree.search_key(self.btree.root, 6))

    def test_linearisation(self):
        expected_keys = [2, 3, 4, 5]
        actual_keys = self.btree.linearisation(self.btree.root)
        self.assertEqual(actual_keys, expected_keys)

    def test_insert(self):
        self.btree.insert(1)
        self.assertTrue(self.btree.search_key(self.btree.root, 1))
        self.btree.insert(6)
        self.assertTrue(self.btree.search_key(self.btree.root, 6))

        expected_keys = [1, 2, 3, 4, 5, 6]
        actual_keys = self.btree.linearisation(self.btree.root)
        self.assertEqual(actual_keys, expected_keys)

if __name__ == '__main__':
    unittest.main()