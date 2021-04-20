import unittest

from src.min_stack import Stack


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)
        self.assertEqual(len(self.stack), 0)
        with self.assertRaises(RuntimeError):
            self.stack.pop()

    def test_push_pop(self):
        for data in [3, 5, 2, 1]:
            self.stack.push(data)
        for data in reversed([3, 5, 2, 1]):
            self.assertEqual(data, self.stack.pop())

    def test_min(self):
        for data in [3, 5, 2, 1]:
            self.stack.push(data)
        for data in [1, 2, 3, 3]:
            self.assertEqual(data, self.stack.min())
            self.stack.pop()


if __name__ == '__main__':
    unittest.main()
