class AVL:
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
        if value < node.value:
            if node.left == None:
                return node
            return self._find(node.left, value)
        if value > node.value:
            if node.right == None:
                return node
            return self._find(node.right, value)


    def insert(self, value):
        if self._root == None:
            self._root = AVL.Node(value)
        new_parent = self._find(self._root, value)
        if new_parent.value == value:
            return
        if value < new_parent.value:
            new_parent.left = AVL.Node(value)
            new_parent.left.parent = new_parent
        if value > new_parent.value:
            new_parent.right = AVL.Node(value)
            new_parent.right.parent = new_parent
        pass


    def _checkBalance(self, node):
        balance = node.getBalance()
        if balance == 0:
            return
        if abs(balance) == 1:
            node.updateHeight()
            if node.parent == None:
                return
            else:
                self._checkBalance(node.parent)
        if balance == -2:
            self._balance(-2)
            return
        if balance == 2:
            self._balance(2)
            return
        raise ValueError()

    def _balance(self, balance):
        pass