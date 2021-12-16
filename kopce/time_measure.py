import gc
import time

def get_time_insert(heap, list, rep):
    timey = 0
    for i in range(rep):
        heap.clean()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for elem in list:
            heap.insert_value(elem)
        stop = time.process_time()
        gc.enable()
        timey += stop - start
    return timey/rep

def get_time_delete(heap, number, rep):
    timey = 0
    for i in range(rep):
        heap_copy = heap.copy()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in range(number):
            heap_copy.delete_root()
        stop = time.process_time()
        gc.enable()
        timey += stop - start
    return timey/rep
