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
            return root
        prev, first = None, None
        def dfs(root):
            nonlocal prev, first
            if not root:
                return 
            
            dfs(root.left)
            if not prev:
                first = root
            else:
                root.left = prev
                prev.right = root
            prev = root
            
            dfs(root.right)
        
        dfs(root)
        first.left = prev
        prev.right = first
        return first
            