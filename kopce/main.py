from binary_heap import BinaryHeap
from n_ary_heap import NHeap
from random import randint
from time_measure import get_time_insert, get_time_delete
from drawing_plots import draw_a_plot
import sys

sys.setrecursionlimit(3000)


list = []
for i in range(0, 100001):
    val = randint(0, 1500000)
    while val in list:
        val = randint(0, 1500000)
    list.append(val)

checkpoints = [i for i in range(10000, 100001, 10000)]

heap_2_times = ([], [])       # insert, delete
heap_3_times = ([], [])
heap_4_times = ([], [])

for n in checkpoints:

    heap_2 = BinaryHeap()
    heap_3 = NHeap(3)
    heap_4 = NHeap(4)

    new_list = list[:n]

    heap_2_times[0].append(get_time_insert(heap_2, new_list))
    heap_2_times[1].append(get_time_delete(heap_2, n))

    heap_3_times[0].append(get_time_insert(heap_3, new_list))
    heap_3_times[1].append(get_time_delete(heap_3, n))

    heap_4_times[0].append(get_time_insert(heap_4, new_list))
    heap_4_times[1].append(get_time_delete(heap_4, n))
    print(n, "iteration")

draw_a_plot(checkpoints, heap_2_times[0], heap_3_times[0], heap_4_times[0], "creating")
draw_a_plot(checkpoints, heap_2_times[1], heap_3_times[1], heap_4_times[1], "deleting root")
