def SelectionSort(list):
    for it in range(0, len(list)):
        min_index = it
        for index in range(it+1, len(list)):
            if list[index] < list[min_index]:
                min_index = index
        list[it], list[min_index] = list[min_index], list[it]