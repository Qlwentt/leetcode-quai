# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pFound = False
        qFound = False
        
        def dfs(root):
            nonlocal pFound, qFound
            if not root:
                return None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root == p:
                pFound = True
                return root
            
            if root == q:
                qFound = True
                return root

            if left and right:
                return root
            if not left:
                return right
            if not right:
                return left
            
        lca = dfs(root)
        return lca if (pFound and qFound) else None
                
            
        