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
        inorder = []
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
        dfs(root)
        
        for i,node in enumerate(inorder):
            node.right = inorder[i+1] if i < len(inorder) -1 else inorder[0]
            node.left = inorder[i-1] if i > 0 else inorder[-1]
        
        return inorder[0]
            
            