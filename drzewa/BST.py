
class Node:
    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None

class BST:

    def __init__(self):
        self.root=None
    
    # inserting an element
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

    # searching an element
    # method returns an instance of Node with given value
    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return None
    
    def _search(self, value, cur_node):
        if value==cur_node.value:
            return cur_node
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

    # displaying a tree
    def _print2D(self, root, space):
        
        COUNT = [10]

        # Base case
        if (root == None) :
            return
    
        # Increase distance between levels
        space += COUNT[0]
    
        # Process right child first
        self._print2D(root.right_child, space)
    
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(root.value)
    
        # Process left child
        self._print2D(root.left_child, space)
    
    def print2D(self) :
        
        # space=[0]
        # Pass initial space count as 0
        self._print2D(self.root, 0)

    def delete_value(self, value):
        return self.delete_node(self.search(value))
    
    def delete_node(self,node):

		# deleting a node not found in the tree
        if node==None or self.search(node.value)==None:
            print("Node to be deleted not found in the tree!")
            return None 

		# node with min value in tree rooted at input node
        def min_value_node(n):
            current=n
            while current.left_child!=None:
                current=current.left_child
            return current

        # number of children for the specified node
        def num_children(n):
            num_children=0
            if n.left_child!=None: num_children+=1
            if n.right_child!=None: num_children+=1
            return num_children

        node_parent=node.parent

        node_children=num_children(node)

        # CASE 1 (node has no children)
        if node_children==0:

            if node_parent!=None:
                # remove reference to the node from the parent
                if node_parent.left_child==node:
                    node_parent.left_child=None
                else:
                    node_parent.right_child=None
            else:
                self.root=None

        # CASE 2 (node has a single child)
        if node_children==1:

            if node.left_child!=None:
                child=node.left_child
            else:
                child=node.right_child

            if node_parent!=None:
                # replace the node to be deleted with its child
                if node_parent.left_child==node:
                    node_parent.left_child=child
                else:
                    node_parent.right_child=child
            else:
                self.root=child

            # correct the parent pointer in node
            child.parent=node_parent

            # CASE 3 (node has two children)
        if node_children==2:

            # get the inorder successor of the deleted node
            successor=min_value_node(node.right_child)

            # copy the inorder successor's value
            node.value=successor.value

            # delete the inorder successor
            self.delete_node(successor)