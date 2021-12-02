class Node:
        def __init__(self, value):
            self.value = value
            self.parent = None
            self.left = None
            self.right = None
            self.height = 0

        def getBalance(self):
            if self.left == None:
                l_height = -1
            else:
                l_height = self.left.height
            if self.right == None:
                r_height = -1
            else:
                r_height = self.right.height
            return r_height - l_height

        def updateHeight(self):
            if self.left == None:
                l_height = -1
            else:
                l_height = self.left.height
            if self.right == None:
                r_height = -1
            else:
                r_height = self.right.height
            self.height = max(l_height, r_height) + 1


class AVL:

    def __init__(self):
        self._root = None


    def find(self, value):
        '''
        Metoda wyszukuje i zwraca obiekt Node ktory zawiera poszukiwana wartosc.
        Jezeli nie ma takiej wartosci w drzewie metoda zwraca wezel, do ktorego
        powinien zostac powiazany obiekt z szukana wartoscia
        '''
        if self._root == None:
            return None
        return self._find(self._root, value)


    def _find(self, node, value):
        if node == None:
            return None
        if value == node.value:
            return node
        elif value < node.value:
            if node.left == None:
                return node
            return self._find(node.left, value)
        else:
            if node.right == None:
                return node
            return self._find(node.right, value)


    def insert(self, value):
        if self._root == None:
            self._root = Node(value)
            return
        new_parent = self._find(self._root, value)
        if new_parent.value == value:
            return
        elif value < new_parent.value:
            new_parent.left = Node(value)
            new_parent.left.parent = new_parent
        else:
            new_parent.right = Node(value)
            new_parent.right.parent = new_parent
        self._checkBalance(new_parent)


    def _checkBalance(self, node):
        node.updateHeight()
        balance = node.getBalance()
        if balance == 0:
            return node.parent
        elif abs(balance) == 1:
            # node.updateHeight()
            if node.parent == None:
                return node.parent
            else:
                self._checkBalance(node.parent)
        elif balance <= -2:
            self._balance(node, -2)
            if node.parent == None:
                return node.parent
            else:
                self._checkBalance(node.parent)
        elif balance >= 2:
            self._balance(node, 2)
            if node.parent == None:
                return node.parent
            else:
                self._checkBalance(node.parent)



    def _balance(self, node, balance):
        if balance == -2:
            if node.left.getBalance() == -1:
                self._rotateRight(node)
            elif node.left.getBalance() == 1:
                self._rotateLeft(node.left)
                self._rotateRight(node)
            else:
                self._rotateRight(node)
        if balance == 2:
            if node.right.getBalance() == 1:
                self._rotateLeft(node)
            elif node.right.getBalance() == -1:
                self._rotateRight(node.right)
                self._rotateLeft(node)
            else:
                self._rotateLeft(node)


    def _rotateLeft(self, node):
        parent = node.parent
        r = node.right
        rl = node.right.left
        r.left = node
        node.right = rl
        if rl != None:
            rl.parent = node
        node.parent = r
        r.parent = parent
        if parent != None:
            if parent.value > r.value:
                parent.left = r
            else:
                parent.right = r
        else:
            self._root = r
        node.updateHeight()
        r.updateHeight()


    def _rotateRight(self, node):
        parent = node.parent
        l = node.left
        lr = node.left.right
        l.right = node
        node.left = lr
        if lr != None:
            lr.parent = node
        node.parent = l
        l.parent = parent
        if parent != None:
            if parent.value > l.value:
                parent.left = l
            else:
                parent.right = l
        else:
            self._root = l
        node.updateHeight()
        l.updateHeight()

    def delete(self, value):
        element = self.find(value)
        if element == None or element.value != value:   # nie ma takiej wartosci w drzewie
            return
        self._delete(element)

    def _delete(self, element):
        left_child = element.left
        right_child = element.right
        parent = element.parent
        #przypadek 1: usuwany element jest lisciem
        if left_child == None and right_child == None:
            if parent == None:
                self._root = None
                return
            else:
                if parent.value > element.value:
                    parent.left = None
                else:
                    parent.right = None
                parent.updateHeight()
                next_to_check = self._checkBalance(parent)
                while(next_to_check != None):                   # checkBalance w przypadku gdy balance = 0 nie sprawdzi kolejnego rodzica
                    next_to_check = self._checkBalance(next_to_check)  # przy usuwaniu musimy jednak sprawdzic cala sciezke, wiec potrzebna nam ta petla
                return

        #przypadek 2: usuwany element ma tylko lewego dziedzica
        elif right_child == None and left_child != None:
            if parent == None:
                left_child.parent = None
                self._root = left_child
                return
            else:
                left_child.parent = parent
                if parent.value > element.value:
                    parent.left = left_child
                else:
                    parent.right = left_child
                parent.updateHeight()
                next_to_check = self._checkBalance(parent)
                while(next_to_check != None):
                    next_to_check = self._checkBalance(next_to_check)

        #przypadek 3: usuwany element ma tylko prawego dziedzica
        elif left_child == None and right_child != None:
            if parent == None:
                right_child.parent = None
                self._root = right_child
                return
            else:
                right_child.parent = parent
                if parent.value > element.value:
                    parent.left = right_child
                else:
                    parent.right = right_child
                parent.updateHeight()
                next_to_check = self._checkBalance(parent)
                while(next_to_check != None):
                    next_to_check = self._checkBalance(next_to_check)

        #przypadek 4: usuwany element ma obu dziedziców
        else:
            # najpierw znajdujemy nastepnika
            next = left_child
            while(next.right != None):
                next = next.right
            value = next.value   # zapamietujemy jego wartosc, aby pozniej wstawic ja w miejsce usuwanego elementu
            self._delete(next)   # usuwamy nastepnika
            element.value = value   # zamieniamy wartosc elementu ktory chcielismy usunac na wartosc nastepnika


    def _print2D(self, root, space):

        COUNT = [10]

        # Base case
        if (root == None) :
            return

        # Increase distance between levels
        space += COUNT[0]

        # Process right child first
        self._print2D(root.right, space)

        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(root.value)

        # Process left child
        self._print2D(root.left, space)

    def print2D(self) :

        # space=[0]
        # Pass initial space count as 0
        print("--------------------------------")
        self._print2D(self._root, 0)
        print("--------------------------------")


    def getRoot(self):
        return self._root.value