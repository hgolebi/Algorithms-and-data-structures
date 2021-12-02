import gc
import time

def getTime(tree, tree_type, list, operation):
    gc_old = gc.isenabled()
    gc.disable()
    if operation == 'insert':
        start = time.process_time()
        for elem in list:
            tree.insert(elem)
        stop = time.process_time()
        return stop - start

    if tree_type == 'BST':
        if operation == 'delete':
            start = time.process_time()
            for elem in list:
                tree.delete_value(elem)
            stop = time.process_time()
            return stop - start

        if operation == 'search':
            start = time.process_time()
            for elem in list:
                tree.search(elem)
            stop = time.process_time()
            return stop - start

    if tree_type == 'AVL':
        if operation == 'delete':
            start = time.process_time()
            for elem in list:
                tree.delete(elem)
            stop = time.process_time()
            return stop - start

        if operation == 'search':
            start = time.process_time()
            for elem in list:
                tree.find(elem)
            stop = time.process_time()
            return stop - start

    gc.enable()