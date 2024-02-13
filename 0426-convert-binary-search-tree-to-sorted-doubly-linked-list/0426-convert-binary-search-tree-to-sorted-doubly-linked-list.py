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
        first = None
        prev = None
        
        if not root:
            return root
        
        def inorder(root):
            nonlocal first, prev
            if not root:
                return
            
            inorder(root.left)
            if prev == None:
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