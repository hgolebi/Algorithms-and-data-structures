arr = [2, 31, 2, 1 ,23, 0, 4, 3]

def SelectionSort(list):
    it = 0
    while(it < len(list)-1):
        min_index = it
        for index in range(it+1, len(list)):
            if list[index] < list[min_index]:
                min_index = index
        temp = list[it]
        list[it] = list[min_index]
        list[min_index] = temp
        it += 1

SelectionSort(arr)
print(arr)