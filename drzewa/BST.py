
class Node:
    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None

class BST:
    def __init__(self):
        self.root=None
    
    # wstawianie elementu
    def insert(self, value):
        if self.root==None:
            self.root=Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=Node(value)
                cur_node.left_child.parent=cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child=Node(value)
                cur_node.right_child.parent=cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print(value + " is already in tree")

    # wyszukiwanie elementu
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return None
    
    def _search(self, value, cur_node):
        if value==cur_node.value:
            return cur_node.value
        if value<cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        if value>cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)
        return None

    def print_tree(self, k1, k2):
        if self.root != None:
            self._print_tree(self.root, k1, k2)
        return
    
    def _print_tree(self, cur_node, k1, k2):
        if cur_node == None:
            return
        if k1 < cur_node.value:
            self._print_tree(cur_node.left_child, k1, k2)
    
        if k1 <= cur_node.value and k2 >= cur_node.value:
            print(cur_node.value)
    
        self._print_tree(cur_node.right_child, k1, k2)