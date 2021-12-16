from n_ary_heap import NHeap
from random import shuffle

list = list(range(0,25))
shuffle(list)
heap = NHeap(2)

for elem in list:
    heap.insert_value(elem)
    print('inserting: ', elem)
    heap.print()

for elem in list:
    pop = heap.delete_root()
    heap.print()
    print('popped element: ', pop)
