import unittest

from src.heap import Heap, HeapTypes


class MyTestCase(unittest.TestCase):
    def test_min_heap_size_at_creation(self):
        heap = Heap()
        self.assertEqual(heap.size, 0)

    def test_min_heap_push(self):
        heap = Heap()
        for i in [2, 5, 6, 1, 6]:
            heap.push(i)
        self.assertEqual(heap.size, 5)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 6)

    def test_min_heapify(self):
        heap = Heap()
        heap.heapify([2, 5, 6, 1, 6])
        self.assertEqual(heap.size, 5)
        self.assertEqual(heap.pop(), 1)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 6)

    def test_min_heap_push_with_list_key(self):
        heap = Heap(key=lambda x: x[1])
        for i in [[0, 30], [15, 20], [5, 10]]:
            heap.push(i)
        for _first, _second in [[5, 10], [15, 20], [0, 30]]:
            first, second = heap.pop()
            self.assertEqual(first, _first)
            self.assertEqual(second, _second)

    def test_min_heap_push_with_set_key(self):
        heap = Heap(key=lambda x: x[1])
        for i in [(0, 30), (15, 20), (5, 10)]:
            heap.push(i)
        for _first, _second in [[5, 10], [15, 20], [0, 30]]:
            first, second = heap.pop()
            self.assertEqual(first, _first)
            self.assertEqual(second, _second)

    def test_min_heap_push_with_dict_key(self):
        some_dictionaries = [{"string": "Four", "numeric": 4},
                             {"string": "Twenty", "numeric": 20},
                             {"string": "Nineteen", "numeric": 19}]
        heap = Heap(key=lambda x: x['numeric'])
        for i in some_dictionaries:
            heap.push(i)
        self.assertEqual(heap.pop()['string'], 'Four')
        self.assertEqual(heap.pop()['string'], 'Nineteen')
        self.assertEqual(heap.pop()['string'], 'Twenty')

    def test_min_heap_push_with_object_key(self):
        class Data:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        some_objects = [Data("John", 20), Data("Jane", 18), Data("Jude", 56)]
        heap = Heap(key=lambda x: x.age)
        for i in some_objects:
            heap.push(i)
        self.assertEqual(heap.pop().name, 'Jane')
        self.assertEqual(heap.pop().name, 'John')
        self.assertEqual(heap.pop().name, 'Jude')

    def test_max_heap_push(self):
        heap = Heap(heap_type=HeapTypes.MAX)
        for i in [2, 5, 6, 1, 6]:
            heap.push(i)
        self.assertEqual(heap.size, 5)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 1)

    def test_max_heapify(self):
        heap = Heap(heap_type=HeapTypes.MAX)
        heap.heapify([2, 5, 6, 1, 6])
        self.assertEqual(heap.size, 5)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 6)
        self.assertEqual(heap.pop(), 5)
        self.assertEqual(heap.pop(), 2)
        self.assertEqual(heap.pop(), 1)

    def test_max_heap_push_with_list_key(self):
        heap = Heap(key=lambda x: x[1], heap_type=HeapTypes.MAX)
        for i in [[0, 30], [15, 20], [5, 10]]:
            heap.push(i)
        for _first, _second in [[0, 30], [15, 20], [5, 10]]:
            first, second = heap.pop()
            self.assertEqual(first, _first)
            self.assertEqual(second, _second)

    def test_max_heap_push_with_set_key(self):
        heap = Heap(key=lambda x: x[1], heap_type=HeapTypes.MAX)
        for i in [(0, 30), (15, 20), (5, 10)]:
            heap.push(i)
        for _first, _second in [[0, 30], [15, 20], [5, 10]]:
            first, second = heap.pop()
            self.assertEqual(first, _first)
            self.assertEqual(second, _second)

    def test_max_heap_push_with_dict_key(self):
        some_dictionaries = [{"string": "Four", "numeric": 4},
                             {"string": "Twenty", "numeric": 20},
                             {"string": "Nineteen", "numeric": 19}]
        heap = Heap(key=lambda x: x['numeric'], heap_type=HeapTypes.MAX)
        for i in some_dictionaries:
            heap.push(i)
        self.assertEqual(heap.pop()['string'], 'Twenty')
        self.assertEqual(heap.pop()['string'], 'Nineteen')
        self.assertEqual(heap.pop()['string'], 'Four')

    def test_max_heap_push_with_object_key(self):
        class Data:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        some_objects = [Data("John", 20), Data("Jane", 18), Data("Jude", 56)]
        heap = Heap(key=lambda x: x.age, heap_type=HeapTypes.MAX)
        for i in some_objects:
            heap.push(i)
        self.assertEqual(heap.pop().name, 'Jude')
        self.assertEqual(heap.pop().name, 'John')
        self.assertEqual(heap.pop().name, 'Jane')

    def test_min_heap_top_n(self):
        heap = Heap(heap_type=HeapTypes.MIN)
        heap.heapify([2, 5, 6, 1, 6])
        self.assertEqual(5, len(heap))
        for x, y in zip(heap.top_n(3), [1, 2, 5]):
            self.assertEqual(x, y)
        self.assertEqual(5, len(heap))

    def test_max_heap_top_n(self):
        heap = Heap(heap_type=HeapTypes.MAX)
        heap.heapify([2, 5, 6, 1, 6])
        self.assertEqual(5, len(heap))
        for x, y in zip(heap.top_n(3), [6, 6, 5]):
            self.assertEqual(x, y)
        self.assertEqual(5, len(heap))

    def test_max_heap_iteration(self):
        heap = Heap(heap_type=HeapTypes.MAX)
        heap.heapify([2, 5, 6, 1, 6])
        for x, y in zip(heap, [6, 6, 5, 2, 1]):
            self.assertEqual(y, y)


if __name__ == '__main__':
    unittest.main()
