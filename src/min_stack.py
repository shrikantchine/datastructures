class Stack:
    def __init__(self):
        self._stack = []
        self._min = None

    def push(self, data):
        if self.is_empty():
            self._stack.append(data)
            self._min = data
        else:
            if data >= self._min:
                self._stack.append(data)
            else:
                self._stack.append(2 * data - self._min)
                self._min = data

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack underflow")
        data = self._stack.pop()
        if data >= self._min:
            return data
        tmp = self._min
        self._min = 2 * self._min - data
        return tmp

    def min(self):
        return self._min

    def size(self):
        return len(self)

    def is_empty(self):
        return self.size() == 0

    def __len__(self):
        return len(self._stack)
