from merge_sort import merge_sort
from bubble_sort import bubble_sort
from readfile import GetWordsList
from quicksort import QuickSort
from selection_sort import SelectionSort
import timeit

from matplotlib import pyplot as plt

def draw_a_plot(x, y, sort_type):
    plt.plot(x, y, marker='o')
    plt.suptitle(sort_type+" - time complexity")
    plt.ylabel("Measured time (s)")
    plt.xlabel("Number of sorted words")
    plt.savefig(sort_type+'.png')
    plt.clf()

file_path = 'pan-tadeusz-nowy.txt'
words_number=[]
for i in range(1000, 10001, 1000):
    words_number.append(i)
time_bubble=[]
time_selection=[]
time_merge=[]
time_quick=[]

# bubble sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    measured_time = timeit.timeit(lambda: bubble_sort(arr), number=10)
    measured_time/=10
    time_bubble.append(measured_time)

draw_a_plot(words_number, time_bubble, "Bubble sort")

# selection sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    measured_time = timeit.timeit(lambda: SelectionSort(arr), number=10)
    measured_time/=10
    time_selection.append(measured_time)

draw_a_plot(words_number, time_selection, "Selection sort")

# merge sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    measured_time = timeit.timeit(lambda: merge_sort(arr), number=1000)
    measured_time/=1000
    time_merge.append(measured_time)

draw_a_plot(words_number, time_merge, "Merge sort")

# quick sort
for number in words_number:
    arr = GetWordsList(file_path, number)
    measured_time = timeit.timeit(lambda: QuickSort(arr), number=1000)
    measured_time/=1000
    time_quick.append(measured_time)

draw_a_plot(words_number, time_quick, "Quick sort")

# merge i sort na jednym wykresie
plt.plot(words_number, time_merge, marker='o', label='Merge sort')
plt.plot(words_number, time_quick, marker='o', label='Quick sort')
plt.legend(prop={'size':8})
plt.suptitle("Merge & Quick sort - time complexity")
plt.ylabel("Measured time (s)")
plt.xlabel("Number of sorted words")
plt.savefig('Merge&Quick.png')
plt.clf()

# wszystkie na jednym wykresie
plt.plot(words_number, time_bubble, marker='o', label='Bubble sort')
plt.plot(words_number, time_selection, marker='o', label='Selection sort')
plt.plot(words_number, time_merge, marker='o', label='Merge sort')
plt.plot(words_number, time_quick, marker='o', label='Quick sort')
plt.legend(prop={'size':8})
plt.suptitle("All sorting types - time complexity")
plt.ylabel("Measured time (s)")
plt.xlabel("Number of sorted words")
plt.savefig('All-in-one-v1.png')
plt.ylim(0, 0.5)
plt.savefig('All-in-one-v2.png')
plt.clf()


with open("czasy.txt", "w") as pom_czasowe:
    pom_czasowe.write("\nbubble: "+str(time_bubble))
    pom_czasowe.write("\nselection: "+str(time_selection))
    pom_czasowe.write("\nmerge: "+str(time_merge))
    pom_czasowe.write("\nquick: "+str(time_quick))
