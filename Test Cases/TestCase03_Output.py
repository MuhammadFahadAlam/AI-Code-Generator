class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root is not None:
        print(root.val, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')

# Construct the tree from the provided image
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

# Perform the traversals
print("In-Order Traversal:")
in_order_traversal(root)
print("\nPre-Order Traversal:")
pre_order_traversal(root)
print("\nPost-Order Traversal:")
post_order_traversal(root)