class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def get_parent(self, i):
        return (i-1)//2
    def get_left(self, i):
        return 2*i+1
    def get_right(self, i):
        return 2*i+2
    
    def has_parent(self, i):
        return self.get_parent(i)>=0
    def has_left(self, i):
        return self.get_left(i) < len(self.heap)
    def has_right(self, i):
        return self.get_right(i) < len(self.heap)

    def clean(self):
        self.heap = []
    
    def copy(self):
        new_heap = BinaryHeap()
        new_heap.heap = self.heap.copy()
        return new_heap
    
    #inserting
    def insert_value(self, value):
        self.heap.append(value)
        self._up_heap(len(self.heap)-1)
    
    def _up_heap(self, i):
        temp = self.heap[i]
        while self.has_parent(i) and self.heap[self.get_parent(i)]> temp:
            self.heap[i] = self.heap[self.get_parent(i)]
            i = self.get_parent(i)
        self.heap[i] = temp
    
    #popping
    def delete_root(self):
        if len(self.heap) == 0:
            return Exception
        root = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        del self.heap[len(self.heap)-1]
        self._down_heap(0)
        return root
    
    def _down_heap(self, i):
        while(self.has_left(i)):
            j = self.get_left(i)
            if self.has_right(i) and self.heap[j+1] < self.heap[j]:
                j = j+1
            if self.heap[i] < self.heap[j]: break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    #printing
    def print(self):
        if not self.heap:
            print("Heap is empty!")
            return
        line_length = 128
        print('-' * line_length)
        curr_line = 1
        counter = 0
        line = ''
        for elem in self.heap:
            if counter == curr_line:
                print('\n' + line, '\n')
                line = ''
                curr_line *= 2
                counter = 0
            counter += 1
            space = max(1, line_length // (curr_line * 2) - 1)
            if curr_line > 1 and counter % 2 == 1 :
                line += '|' + ' ' * (space - 1) + str(elem).zfill(2) + ' ' * space
            elif counter % 2 == 0:
                line += ' ' * space + str(elem).zfill(2) + ' ' * (space - 1) + '|'
            else:
                line += ' ' * space + str(elem).zfill(2) + ' ' * space
        print(line, '\n')
        print('-' * line_length)
