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
        # L V R
        prev = None
        first = None
        if not root:
            return root
        def inorder(root):
            nonlocal first, prev
            if not root:
                return
            inorder(root.left)
            if not prev:
                first = root
            else:
                root.left = prev
                prev.right = root
            prev = root
            inorder(root.right)
        inorder(root)    
        first.left = prev
        prev.right = first
        
        return first
            