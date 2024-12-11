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
        
    def get_min(self):
        current = self.root
        if current is None:
            return None
        while current.left is not None:
            current = current.left
        return current.value

    def get_max(self):
        current = self.root
        if current is None:
            return None
        while current.right is not None:
            current = current.right
        return current.value
    
notas = [85, 70, 95, 60, 75, 90, 100]
bst = BinaryTree()

for nota in notas:
    bst.add(nota)

print(f"Min: {bst.get_min()}")
print(f"Max: {bst.get_max()}")