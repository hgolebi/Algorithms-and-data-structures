from merge_sort import merge_sort
from bubble_sort import bubble_sort
from readfile import GetWordsList
from quicksort import QuickSort
import timeit

from sortowanie.selection_sort import SelectionSort

file_path = 'pan-tadeusz-nowy.txt'
words_num=1000
while(words_num<=10000):
    arr = GetWordsList(file_path, words_num)
    merge_time = timeit.timeit(lambda: merge_sort(arr), number=1)
    print("Merge sort execution time for "+str(words_num)+ " words: " + str(merge_time))

    arr = GetWordsList(file_path, words_num)
    bubble_time = timeit.timeit(lambda: bubble_sort(arr), number=1)
    print("Bubble sort execution time for "+str(words_num)+ " words: " + str(bubble_time))

    arr = GetWordsList(file_path, words_num)
    quick_time = timeit.timeit(lambda: QuickSort(arr), number=1)
    print("Quick sort execution time for "+str(words_num)+ " words: " + str(quick_time))

    arr = GetWordsList(file_path, words_num)
    selection_time = timeit.timeit(lambda: SelectionSort(arr), number=1)
    print("Selection sort execution time for "+str(words_num)+ " words: " + str(selection_time))

    words_num += 1000