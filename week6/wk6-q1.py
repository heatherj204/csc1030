class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key > root.val:
        root.right = insert(root.right, key)
        print(f"{key} is to the right of {root.val}")
    elif key < root.val:
        root.left = insert(root.left, key)
        print(f"{key} is to the left of {root.val}")

    return root



# Usage
root = TreeNode(10)
root = insert(root, 5)
root = insert(root, 15)