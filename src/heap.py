import enum


class HeapTypes(enum.Enum):
    MIN = 1
    MAX = 2


class Heap:
    def __init__(self, key=None, heap_type=HeapTypes.MIN):
        self.heap = [-1]
        self.size = 0
        self.key = key
        self.is_min = heap_type == HeapTypes.MIN

    def push(self, data):
        self.size += 1
        self.heap.append(data)
        self._swim(self.size)

    def pop(self):
        if self.size == 0:
            raise RuntimeError("Heap underflow")
        top_val = self.heap[1]
        self._swap(1, self.size)
        self.size -= 1
        self._sink(1)
        del self.heap[self.size + 1]
        return top_val

    def heapify(self, _iterable):
        for data in _iterable:
            self.push(data)

    def top_n(self, n):
        if n > self.size:
            raise RuntimeError("Heap overall")
        results = [self.pop() for _ in range(n)]
        for node in results:
            self.push(node)
        return results

    def _sink(self, k):
        while 2 * k <= self.size:
            j = 2 * k
            if j < self.size and self._compare(j, j + 1):
                j += 1
            if not self._compare(k, j):
                break
            self._swap(k, j)
            k = j

    def _swim(self, k):
        while k > 1 and self._compare(k // 2, k):
            self._swap(k // 2, k)
            k = k // 2

    def _compare(self, x, y):
        x_val = self.key(self.heap[x]) if self.key else self.heap[x]
        y_val = self.key(self.heap[y]) if self.key else self.heap[y]
        return x_val > y_val if self.is_min else x_val < y_val

    def _swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]

    def __iter__(self):
        return iter(self.top_n(self.size))

    def __len__(self):
        return self.size

    def __str__(self):
        return f"Heap: {self.heap[1:]}, type: {'Min' if self.is_min else 'Max'}"

    def __repr__(self):
        return f"Heap: {self.heap[1:]}"
