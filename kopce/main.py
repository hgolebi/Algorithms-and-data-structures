from binary_heap import BinaryHeap
from n_ary_heap import NHeap
#from quaternary_heap import QuaternaryHeap
from random import randint
from time_measure import get_time_insert, get_time_delete
from drawing_plots import draw_a_plot
import sys

sys.setrecursionlimit(3000)


list = []
for i in range(0, 100001):
    val = randint(0, 1500000)
    list.append(val)

checkpoints = [i for i in range(10000, 100001, 10000)]

heap_binary_times = ([], [])    # insert, delete
heap_2_times = ([], [])
heap_3_times = ([], [])
heap_4_times = ([], [])

for n in checkpoints:

    heap_binary = BinaryHeap()
    heap_2 = NHeap(2)
    heap_3 = NHeap(3)
    heap_4 = NHeap(4)

    new_list = list[:n]

    heap_binary_times[0].append(get_time_insert(heap_binary, new_list, 1))
    heap_binary_times[1].append(get_time_delete(heap_binary, n, 7))

    heap_2_times[0].append(get_time_insert(heap_2, new_list, 1))
    heap_2_times[1].append(get_time_delete(heap_2, n, 7))

    heap_3_times[0].append(get_time_insert(heap_3, new_list, 1))
    heap_3_times[1].append(get_time_delete(heap_3, n, 7))

    heap_4_times[0].append(get_time_insert(heap_4, new_list, 1))
    heap_4_times[1].append(get_time_delete(heap_4, n, 7))
    print(n, "iteration")

draw_a_plot(checkpoints, heap_2_times[0], heap_3_times[0], heap_4_times[0], heap_binary_times[0], "creating")
draw_a_plot(checkpoints, heap_2_times[1], heap_3_times[1], heap_4_times[1], heap_binary_times[1], "deleting root")
