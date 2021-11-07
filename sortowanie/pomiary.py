from merge_sort import merge_sort
from bubble_sort import bubble_sort
from readfile import GetWordsList
import timeit

words_num=1000
while(words_num<=10000):
    arr = GetWordsList('pan-tadeusz-nowy.txt', words_num)
    merge_time = timeit.timeit(lambda: merge_sort(arr), number=1)
    print("Merge sort execution time for "+str(words_num)+ " words: " + str(merge_time))

    arr = GetWordsList('pan-tadeusz-nowy.txt', words_num)
    bubble_time = timeit.timeit(lambda: bubble_sort(arr), number=1)
    print("Bubble sort execution time for "+str(words_num)+ " words: " + str(bubble_time))

    words_num += 1000