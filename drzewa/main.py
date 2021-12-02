import random
from BST import BST, Node
from AVL import AVL
from random import randrange, shuffle, randint
from time_measure import getTime
import sys

sys.setrecursionlimit(3000)


list = []
for i in range(0, 50001):
    val = randint(0, 1000000)
    while val in list:
        val = randint(0, 1000000)
    list.append(val)

checkpoints = [5000*(i+1) for i in range(0, 10)]

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

    bst_times[0].append(getTime(bst_tree, 'BST', new_list, 'insert'))
    bst_times[1].append(getTime(bst_tree, 'BST', find_list, 'search'))
    bst_times[2].append(getTime(bst_tree, 'BST', del_list, 'delete'))

    avl_times[0].append(getTime(avl_tree, 'AVL', new_list, 'insert'))
    avl_times[1].append(getTime(avl_tree, 'AVL', find_list, 'search'))
    avl_times[2].append(getTime(avl_tree, 'AVL', del_list, 'delete'))
    print(n, "iteration")

for i in range(0, 3):
    print(bst_times[i])

for i in range(0, 3):
    print(avl_times[i])