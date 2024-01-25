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
        first = None
        prev = None
        
        # left = prev
        # right = next
        
        def dfs(root):
            nonlocal first, prev
            if not root:
                return
            
            dfs(root.left)
            if not prev:
                first = root
            else:
                prev.right = root
                root.left = prev
            prev = root
            dfs(root.right)
        dfs(root)    
        first.left = prev
        prev.right = first
        
        return first
        