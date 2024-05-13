class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_min(node: BinaryTree) -> BinaryTree:
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node

def find_successor(node: BinaryTree) -> BinaryTree:

    if node.right is not None:
        return find_min(node.right)

    current_node = node
    while current_node.parent is not None and current_node == current_node.parent.right:
        current_node = current_node.parent

    return current_node.parent

def insert(node, value):
    if node is None:
        return BinaryTree(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


