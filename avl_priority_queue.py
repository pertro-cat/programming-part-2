class Node:
    def __init__(self, value, priority, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right
        self.height = 1

class AVLPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        self.root = self._insert(self.root, value, priority)

    def _insert(self, node, value, priority):
        if not node:
            return Node(value, priority)
        elif priority > node.priority:
            node.left = self._insert(node.left, value, priority)
        else:
            node.right = self._insert(node.right, value, priority)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._balance(node)

        if balance > 1 and priority > node.left.priority:
            return self._rotate_right(node)
        if balance < -1 and priority <= node.right.priority:
            return self._rotate_left(node)
        if balance > 1 and priority <= node.left.priority:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and priority > node.right.priority:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T3 = x.right
        y.left = T3
        x.right = y
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        return x

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def remove(self):
        if self.root is None:
            return None
        value = self.root.value
        self.root = self._remove(self.root)
        return value

    def _remove(self, node):
        if node.left is None:
            return node.right
        node.left = self._remove(node.left)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._balance(node)
        if balance < -1 and self._balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance < -1 and self._balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def peek(self):
        if self.root is None:
            return None
        return self.root.value

    def traverse(self, node):
        if node is None:
            return []
        result = [node.value]
        result.extend(self.traverse(node.left))
        result.extend(self.traverse(node.right))
        return result