import random
from BST import BST, Node
from AVL import AVL
from random import randrange, shuffle
import time
import gc

list = []
for i in range(0, 10001):
    val = randrange(50000)
    while val in list:
        val = randrange(50000)
    list.append(val)

checkpoints = [1000*(i+1) for i in range(0, 10)]

bst_tree = BST()
avl_tree = AVL()

bst_times = ([], [], [])       # insert, search, delete
avl_times = ([], [], [])

for n in checkpoints:

    new_list = list[:n]
    find_list = new_list.copy()
    shuffle(find_list)
    del_list = new_list.copy()
    shuffle(del_list)

    # BST insert
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in new_list:
        bst_tree.insert(elem)
    stop = time.process_time()
    gc.enable()
    bst_times[0].append(stop - start)

    # BST search
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in find_list:
        bst_tree.search(elem)
    stop = time.process_time()
    bst_times[1].append(stop - start)

    # BST delete
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in del_list:
        bst_tree.delete_value(elem)
    stop = time.process_time()
    bst_times[2].append(stop - start)

    assert(bst_tree.root == None)

    # AVL insert
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in new_list:
        avl_tree.insert(elem)
    stop = time.process_time()
    gc.enable()
    avl_times[0].append(stop - start)

    # AVL search
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in find_list:
        avl_tree.find(elem)
    stop = time.process_time()
    avl_times[1].append(stop - start)

    # AVL delete
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for elem in del_list:
        avl_tree.delete(elem)
    stop = time.process_time()
    avl_times[2].append(stop - start)

    assert(avl_tree._root == None)

for i in range(0, 3):
    print(bst_times[i])

for i in range(0, 3):
    print(avl_times[i])