class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        if value < current.value: 
            return self._search(current.left, value)
        else: 
            return self._search(current.right, value)
    
    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._remove(current.left, value)
        elif value > current.value:
            current.right = self._remove(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            
            min_larger_node = self._get_min(current.right)
            current.value = min_larger_node.value
            current.right = self._remove(current.right, min_larger_node.value)
        return current

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.value)
            self._inorder(current.right, result)


codigos = [45, 25, 65, 20, 30, 60, 70]
bst = BinaryTree()

for codigo in codigos:
    bst.add(codigo)

print("Árvore:", bst.inorder())
bst.remove(20)
print("\nÁrvore:", bst.inorder())
bst.remove(25)
print("\nÁrvore:", bst.inorder())
bst.remove(45)
print("\nÁrvore:", bst.inorder())