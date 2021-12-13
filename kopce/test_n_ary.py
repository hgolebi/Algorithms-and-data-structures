from n_ary_heap import NHeap
from random import shuffle

list = list(range(0,25))
shuffle(list)
heap = NHeap(4)

for elem in list:
    heap.insert(elem)
    print('inserting: ', elem)
    heap.print()

for elem in list:
    pop = heap.pop()
    heap.print()
    print('popped element: ', pop)
