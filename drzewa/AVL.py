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
            self._root = AVL.Node(value)
            return
        new_parent = self._find(self._root, value)
        if new_parent.value == value:
            return
        elif value < new_parent.value:
            new_parent.left = AVL.Node(value)
            new_parent.left.parent = new_parent
        else:
            new_parent.right = AVL.Node(value)
            new_parent.right.parent = new_parent
        self._checkBalance(new_parent)


    def _checkBalance(self, node):
        balance = node.getBalance()
        if balance == 0:
            return
        elif abs(balance) == 1:
            node.updateHeight()
            if node.parent == None:
                return
            else:
                self._checkBalance(node.parent)
        elif balance == -2:
            self._balance(node, -2)
            if node.parent == None:
                return
            else:
                self._checkBalance(node.parent)
        elif balance == 2:
            self._balance(node, 2)
            if node.parent == None:
                return
            else:
                self._checkBalance(node.parent)
        else:
            raise ValueError()


    def _balance(self, node, balance):
        if balance == -2:
            if node.left.getBalance() == -1:
                self._rotateRight(node)
            elif node.left.getBalance() == 1:
                self._rotateLeft(node.left)
                self._rotateRight(node)
            else:
                raise ValueError()
        if balance == 2:
            if node.right.getBalance() == 1:
                self._rotateLeft(node)
            elif node.right.getBalance() == -1:
                self._rotateRight(node.right)
                self._rotateLeft(node)
            else:
                raise ValueError()


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
        #przypadek 1: usuwany element jest lisciem
        if element.left == None and element.right == None:
            if element.parent == None:
                self._root = None
                return
            else:
                if element.parent.value > element.value:
                    element.parent.left = None
                else:
                    element.parent.right = None
                element.parent.updateHeight()
                self._checkBalance(element.parent)
                return

        #przypadek 2: usuwany element ma tylko lewego dziedzica
        elif element.right == None and element.left != None:
            if element.parent == None:
                element.left.parent = None
                self._root = element.left
                return
            else:
                element.left.parent = element.parent
                if element.parent.value > element.value:
                    element.parent.left = element.left
                else:
                    element.parent.right = element.left
                element.parent.updateHeight()
                self._checkBalance(element.parent)

        #przypadek 3: usuwany element ma tylko prawego dziedzica
        elif element.left == None and element.right != None:
            if element.parent == None:
                element.right.parent = None
                self._root = element.right
                return
            else:
                element.right.parent = element.parent
                if element.parent.value > element.value:
                    element.parent.left = element.rigth
                else:
                    element.parent.right = element.right
                element.parent.updateHeight()
                self._checkBalance(element.parent)

        #przypadek 4: usuwany element ma obu dziedziców
        else:
            # najpierw znajdujemy nastepnika
            next = element.right
            while(next.left != None):
                next = next.left
            value = next.value   # zapamietujemy jego wartosc, aby pozniej wstawic ja w miejsce usuwanego elementu
            self._delete(next)   # usuwamy nastepnika
            element.value = value   # zamieniamy wartosc elementu ktory chcielismy usunac na wartosc nastepnika