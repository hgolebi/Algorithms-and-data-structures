import gc
import time

def getTime(heap, list, operation):
    gc_old = gc.isenabled()
    gc.disable()
    if operation == 'insert':
        start = time.process_time()
        for elem in list:
            heap.insert_value(elem)
        stop = time.process_time()
        return stop - start

    if operation == 'delete':
        start = time.process_time()
        for elem in list:
            heap.delete_root(elem)
        stop = time.process_time()
        return stop - start

    gc.enable()
