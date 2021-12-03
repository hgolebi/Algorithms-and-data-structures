from AVL import AVL
from random import choice, randrange, shuffle

list = [randrange(200) for i in range(0, 20)]

del_list = list.copy()
shuffle(del_list)

tree = AVL()

for elem in list:
    tree.insert(elem)
    print("inserting: ", elem)
    tree.print_tree()

for elem in del_list:
    print("searching for: ", elem)
    print("we found: ", tree.find(elem).value) 


for elem in del_list:
    tree.delete(elem)
    print("deleting: ", elem)
    tree.print_tree()