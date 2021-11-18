def bubble_sort(arr):
    length=len(arr)
    for i in range(0, length):
        for j in range(0, length-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr