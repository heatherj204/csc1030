# Question 1
class Position:

    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return f"({self.key}, {self.value})"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def _internal_upsert(self, key, value, node, parent=None):

        if not node:
            return Position(key, value, parent)

        if key < node.key:
            node.left = self._internal_upsert(key, value, node.left, node)
        elif key > node.key:
            node.right = self._internal_upsert(key, value, node.right, node)
        elif key == node.key:
            node.value = value

        return node

    def upsert(self, key, value):

        if self.root is None:
            self.root = Position(key, value)
            return self.root

        return self._internal_upsert(key, value, self.root)

    def _internal_in_order(self, node, inorder_list):

        if not node:
            return

        self._internal_in_order(node.left, inorder_list)
        inorder_list.append(node.key)
        self._internal_in_order(node.right, inorder_list)

    def in_order(self):

        in_order_list = []
        self._internal_in_order(self.root, in_order_list)
        return in_order_list

    def _internal_first(self, node):

        if not node.left:
            return node

        return self._internal_first(node.left)

    def first(self, node=None):
        if not node:
            node = self.root
        return self._internal_first(node)

    def _internal_last(self, node):
        if not node.right:
            return node

        return self._internal_last(node.right)