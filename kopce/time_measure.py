import gc
import time

def get_time_insert(heap, list):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in list:
        heap.insert_value(elem)
    stop = time.process_time()
    gc.enable()
    return stop - start

def get_time_delete(heap, number):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for i in range(number):
        heap.delete_root()
    stop = time.process_time()
    gc.enable()
    return stop - start
