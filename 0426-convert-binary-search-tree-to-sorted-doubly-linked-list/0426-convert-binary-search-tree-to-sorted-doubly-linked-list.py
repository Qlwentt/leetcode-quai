"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        first = None # 1
        prev = None # 5
        def inorder(root):
            nonlocal prev, first
            if not root:
                return

        # L V R
            inorder(root.left)
            if not prev:
                first = root
            else:
                prev.right = root
                root.left = prev
            prev = root
            inorder(root.right)
        inorder(root)
        first.left = prev
        prev.right = first
        return first