from binary_heap import BinaryHeap
from random import randrange

list = [randrange(200) for i in range(0, 15)]

heap = BinaryHeap()

for elem in list:
    print("inserting: ", elem)
    heap.insert_value(elem)
    heap.print_heap()

for elem in range(15):
    print("deleting: ", heap.heap[0])
    heap.delete_root()
    heap.print_heap()
