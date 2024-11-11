class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_valid_bst(root):
    amountLeft = len(root.left)
    amountRight = len(root.right)
    i = 0
    value = False
    while i < amountLeft:
        if root.left[i] < root.val:
            value = True
        elif root.left[i] > root.val:
            value = False
    while i < amountRight:
        if root.right[i] > root.val:
            value = True
        elif root.right[i] < root.val:
            value = False
    return value

# Usage
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(is_valid_bst(root)) # Should return True