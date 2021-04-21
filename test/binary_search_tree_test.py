import unittest
from src.binary_search_tree import BST, TreeNode


class BSTTestCases(unittest.TestCase):
    def test_bst_create(self):
        bst = BST()
        self.assertTrue(bst.is_empty())

    def test_bst_put(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        self.assertEqual(8, bst.root.key)
        self.assertEqual("Eight", bst.root.value)
        self.assertEqual(3, bst.root.left.key)
        self.assertEqual("Three", bst.root.left.value)
        self.assertEqual(4, bst.root.left.right.key)
        self.assertEqual("Four", bst.root.left.right.value)
        self.assertEqual(10, bst.root.right.key)
        self.assertEqual("Ten", bst.root.right.value)

    def test_bst_get(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            self.assertEqual(bst.get(key), val)

    def test_is_bst(self):
        bst = BST()
        bst.root = TreeNode(10, "Ten", TreeNode(11, "Eleven"))
        self.assertFalse(bst.is_bst())
        bst.root = TreeNode(10, "Ten", TreeNode(8, "Eight"))
        self.assertTrue(bst.is_bst())
        bst.root = TreeNode(10, "Ten", None, TreeNode(8, "Eight"))
        self.assertTrue(bst.is_bst())
        bst.root = TreeNode(10, "Ten", None, TreeNode(11, "Eleven"))
        self.assertFalse(bst.is_bst())

    def test_pre_order(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        for actual, expected in zip(bst.pre_order(), [8, 3, 4, 10]):
            self.assertEqual(actual[0], expected)

    def test_post_order(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        for actual, expected in zip(bst.post_order(), [4, 3, 10, 8]):
            self.assertEqual(actual[0], expected)

    def test_in_order(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        for actual, expected in zip(bst.in_order(), [3, 4, 8, 10]):
            self.assertEqual(actual[0], expected)

    def test_level_order(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        for actual, expected in zip(bst.level_order(), [8, 3, 10, 4]):
            self.assertEqual(actual[0], expected)

    def test_height(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        self.assertEqual(2, bst.height())

    def test_min(self):
        bst = BST()
        for key, val in [(8, "Eight"), (10, "Ten"), (3, "Three"), (4, "Four")]:
            bst.put(key, val)
        key, val = bst.get_min()
        self.assertEqual(3, key)
        self.assertEqual("Three", val)


if __name__ == '__main__':
    unittest.main()
