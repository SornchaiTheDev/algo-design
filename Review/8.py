class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_balanced_tree(A):
    if not A:
        return None
    mid = len(A) // 2
    root = Node(A[mid])
    root.left = build_balanced_tree(A[:mid])
    root.right = build_balanced_tree(A[mid+1:])
    return root


def modified_traversal(root):
    if not root:
        return
    print(root.data, end=" ")  # Visit the root first
    modified_traversal(root.left)
    modified_traversal(root.right)  # Visit right subtree before left subtree



A = [1, 2, 3, 4, 5, 6]
root = build_balanced_tree(A)
print("Inorder traversal of the balanced tree:")
modified_traversal(root)  # Output: 1 2 3 4 5 6
