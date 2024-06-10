# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            
            
            if root.left or root.right or root.val:
                return root
            else:
                return None
        
    
        return dfs(root)
        