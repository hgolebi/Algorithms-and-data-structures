class NHeap:
    def __init__(self, n):
        self._heap = []
        self._n = n

    def _parent(self, pos):
        if pos == 0:
            return None
        return (pos-1)//self._n

    def _lowestChild(self, pos):
        child1 = pos*self._n + 1
        if child1 >= len(self._heap):
            return None
        min = child1
        for i in range(1, self._n):
            if child1 + i >= len(self._heap):
                return min
            if self._heap[child1 + i] < self._heap[min]:
                min = child1 + i
        return min


    def pop(self):
        if len(self._heap) == 0:
            print('heap is empty!')
            return None
        pop_value = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._downHeap(0)
        return pop_value

    def insert(self, value):
        self._heap.append(value)
        self._upHeap(len(self._heap) - 1)

    def _upHeap(self, pos):
        temp = self._heap[pos]
        while self._parent(pos) > 0 and self._heap[self._parent(pos)] > temp:
            self._heap[pos] = self._heap[self._parent(pos)]
            pos = self._parent(pos)
        self._heap[pos] = temp

    def _downHeap(self, pos):
        while self._lowestChild(pos) != None and self._heap[self._lowestChild(pos)] < self._heap[pos]:
            low = self._lowestChild(pos)
            self._heap[low], self._heap[pos] = self._heap[pos], self._heap[low]
            pos = low