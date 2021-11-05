def QuickSort(list):
    if len(list) == 1 or len(list) == 0:
        return list
    mid = list[0]
    left = []
    right = []
    for item in list[1:]:
        if item < mid:
            left.append(item)
        else:
            right.append(item)
    sorted_left = QuickSort(left)
    sorted_right = QuickSort(right)
    sorted_list = sorted_left.copy()
    sorted_list.append(mid)
    for item in sorted_right:
        sorted_list.append(item)
    return sorted_list
