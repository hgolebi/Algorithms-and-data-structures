from merge_sort import merge_sort
from bubble_sort import bubble_sort
from readfile import GetWordsList
from quicksort import QuickSort
from selection_sort import SelectionSort
import timeit

from matplotlib import pyplot as plt
import numpy as np

def draw_a_plot(x, y, sort_type):
    plt.plot(x, y)
    plt.suptitle(sort_type+" - time complexity")
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of sorted words")
    plt.show()

file_path = 'pan-tadeusz-nowy.txt'
words_number=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
measured_time=[]

#jak coś to trzeba zamknąć jeden wykres, aby odpalil się kolejny

# bubble sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    merge_time = timeit.timeit(lambda: bubble_sort(arr), number=1)
    measured_time.append(merge_time)

draw_a_plot(words_number, measured_time, "Bubble sort")
measured_time=[]

# selection sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    merge_time = timeit.timeit(lambda: SelectionSort(arr), number=1)
    measured_time.append(merge_time)

draw_a_plot(words_number, measured_time, "Selection sort")
measured_time=[]

# merge sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    merge_time = timeit.timeit(lambda: merge_sort(arr), number=1)
    measured_time.append(merge_time)

draw_a_plot(words_number, measured_time, "Merge sort")
measured_time=[]

# quick sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    merge_time = timeit.timeit(lambda: QuickSort(arr), number=1)
    measured_time.append(merge_time)

draw_a_plot(words_number, measured_time, "Quick sort")
measured_time=[]