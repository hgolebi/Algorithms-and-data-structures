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

    def print(self):
        if self._n == 3:
            line_length = 108
        else:
            line_length = 128
        curr_line = 1
        counter = 0
        line = ''
        for elem in self._heap:
            if counter == curr_line:
                print('\n' + line, '\n')
                line = ''
                curr_line *= self._n
                counter = 0
            counter += 1
            space = line_length // (curr_line * 2) - 1
            if curr_line > 1 and counter % self._n == 1 :
                line += '|' + ' ' * (space - 1) + str(elem).zfill(2) + ' ' * space
            elif counter % self._n == 0:
                line += ' ' * space + str(elem).zfill(2) + ' ' * (space - 1) + '|'
            else:
                line += ' ' * space + str(elem).zfill(2) + ' ' * space
        print(line)

heap = NHeap(3)
heap.print()