from BST import BST
from random import choice, randrange, shuffle

list = [randrange(200) for i in range(0, 20)]
del_list = list.copy()
shuffle(del_list)

tree = BST()

for elem in list:
    tree.insert(elem)
    print("inserting: ", elem)
    tree.print_tree()

for elem in del_list:
    print("searching for: ", elem)
    print("we found: ", tree.search(elem).value) 


for elem in del_list:
    tree.delete_value(elem)
    print("deleting: ", elem)
    tree.print_tree()