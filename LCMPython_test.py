import unittest
from LCMPython import findLCA, Node, findPath


class TestLCM(unittest.TestCase):

    def test_LCM(self):
        root = Node(1)  # g
        root.left = Node(2)  # d
        root.right = Node(3)  # f
        root.left.left = Node(4)  # c
        root.right.right = Node(5)  # e
        root.right.right.left = Node(6)  # b
        root.left.left.right = root.right.right.left  # b
        root.left.left.right.right = Node(7)  # a

        self.assertEqual(findLCA(root, 7, 5), 1)
        self.assertEqual(findLCA(root, 7, 6), 6)
        self.assertEqual(findLCA(root, 3, 4), 1)
        self.assertEqual(findLCA(root, 2, 4), 2)

    def test_LCM_two(self):
        root = Node(1)	# graph found using google
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)

        self.assertEqual(findLCA(root, 2, 3), 1)
        self.assertEqual(findLCA(root, 4, 3), 1)
        self.assertEqual(findLCA(root, 5, 4), 2)
        self.assertEqual(findLCA(root, 2, 5), 2)
